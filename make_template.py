import json, urllib.parse
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
d=json.load(open('/tmp/data.json')); FIX={'50WFV'}
VG={'Heineken':('2026-10-30','2026-11-14'),'Modelo':('2026-11-05','2026-12-02'),'Kof':('2026-11-05','2026-12-02')}
rutas=['Ruta Cardel','Ruta Costa','Por Medida y Promoción']
rows=[]
for r in d['recs']:
    a=d['addr'].get(r['cr'],{}); dir_='' if r['cr'] in FIX else a.get('dir','')
    rows.append((rutas.index(r['ruta']),(r['mpo'] or a.get('mpo','')).upper(),r['tienda'],r,dir_))
rows.sort(key=lambda x:(x[0],x[1],x[2]))
wb=Workbook(); ws=wb.active; ws.title='Recorrido'
H=['Ruta','CR','Tienda','Municipio','Dirección','Coordenadas (pegar de Google Maps)','Orden','Marca','Tipo','Medida (m)','Medida original','Promoción','Vigencia desde','Vigencia hasta','Abrir en Google Maps (solo ayuda)']
ws.append(H)
yel=PatternFill('solid',fgColor='FFF2CC'); hd=PatternFill('solid',fgColor='C8102E')
for c in ws[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=hd; c.alignment=Alignment(wrap_text=True,vertical='center')
for _,mpo,_,r,dir_ in rows:
    v=VG.get(r['marca'],('',''))
    q=(dir_+', '+mpo+', Veracruz, México') if dir_ else 'OXXO '+r['tienda']+', '+mpo+', Veracruz, México'
    ws.append([r['ruta'],r['cr'],r['tienda'],mpo,dir_,'','',r['marca'],r['tipo'],r['medida'],r['orig'],r['promo'] or '',v[0],v[1],'Abrir en Maps'])
    i=ws.max_row; c=ws.cell(i,15); c.hyperlink='https://www.google.com/maps/search/?api=1&query='+urllib.parse.quote(q); c.font=Font(color='0563C1',underline='single')
    for col in (6,7): ws.cell(i,col).fill=yel
    if not dir_: ws.cell(i,5).fill=yel
    ws.cell(i,12).alignment=Alignment(wrap_text=True,vertical='top')
for col,w in zip('ABCDEFGHIJKLMNO',[22,8,26,18,48,30,8,11,9,12,12,60,13,13,22]): ws.column_dimensions[col].width=w
ws.freeze_panes='D2'; ws.auto_filter.ref=ws.dimensions; ws.row_dimensions[1].height=32
dv=DataValidation(type='list',formula1='"Heineken,Modelo,Kof"',allow_blank=False); ws.add_data_validation(dv); dv.add(f'H2:H{ws.max_row}')
i=wb.create_sheet('Instrucciones')
for t in ['CÓMO USAR ESTE EXCEL','',
'1. Cada fila es UN espacio a instalar (una tienda con 2 espacios tiene 2 filas). Puedes agregar, borrar o corregir filas.',
'2. Columnas amarillas = por completar. "Coordenadas": en la columna O toca "Abrir en Maps", mantén presionado el lugar correcto en el mapa, copia los números que aparecen (ej. 19.1234, -96.1234) y pégalos en la columna F.',
'   También sirve pegar el enlace largo de Google Maps (el que contiene @19.12,-96.12).',
'3. "Orden" (opcional): número de visita dentro de cada ruta (1, 2, 3…). Si lo dejas vacío, la app ordena por municipio y código postal.',
'4. Para agregar rutas nuevas, escribe otro nombre en "Ruta". Marca: Heineken, Modelo o Kof. Medida con formato 1.35 x 4.85.',
'5. Vigencia en formato AAAA-MM-DD (ej. 2026-11-14).',
'6. No cambies los nombres de los encabezados de la hoja "Recorrido".',
'7. Guarda el archivo y en la app pulsa "📥 Cargar Excel". La app reemplaza los datos y crea el sistema completo.',
'8. Las tiendas SIN coordenadas igual aparecen en la lista y se navegan con Google Maps; solo no salen en el mapa propio.']:
    i.append([t])
i['A1'].font=Font(bold=True,size=14); i.column_dimensions['A'].width=130
wb.save('/home/claude/app/Plantilla_Recorrido.xlsx'); print(len(rows))
