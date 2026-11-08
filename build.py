import json
from defaults import ins,mat
from rutas_def import CARDEL,COSTA,VERACRUZ
d=json.load(open('data_origen.json'))
recs=d['recs']
VG={'Heineken':('2026-10-30','2026-11-14'),'Modelo':('2026-11-05','2026-12-02'),'Kof':('2026-11-05','2026-12-02')}
for i,r in enumerate(recs):
    r['id']=i;r['desde'],r['hasta']=VG[r['marca']]
    a=d['addr'].get(r['cr'],{})
    if not r['mpo']: r['mpo']=a.get('mpo','')
    r['tienda']=r['tienda'].strip()
    r['promo']=r['promo'] or ''
    r['acc']='Instalar';r['ins']=ins(r);r['mat']=mat(r);r['acs']=''
vz=set(VERACRUZ);cs=set(COSTA)
for r in recs:
    if r['ruta']=='Por Medida y Promoción': r['ruta']='Ruta Veracruz' if r['cr'] in vz else ('Ruta Costa' if r['cr'] in cs else 'Otras tiendas')
rutas=['Ruta Cardel','Ruta Costa','Ruta Veracruz','Otras tiendas']
order={'Ruta Cardel':[c for c in CARDEL if c],'Ruta Costa':list(COSTA),'Ruta Veracruz':list(VERACRUZ)}
used={r['cr'] for r in recs}
FIX=['50WFV']  # Cerro Gordo JAL traía la dirección de El Hatito (50R7X)
for c in FIX: d['addr'][c]['dir']=''
addr={k:{'dir':v['dir'],'mpo':v['mpo']} for k,v in d['addr'].items() if k in used}
data=json.dumps(dict(rutas=rutas,recs=recs,addr=addr,fix=FIX,main=rutas[:3],order=order),ensure_ascii=False,separators=(',',':'))
json.dump(dict(rutas=rutas,recs=recs,addr=addr,order=order),open('data_app.json','w'),ensure_ascii=False)
open('index.html','w').write(open('template.html').read().replace('/*DATA*/',data))
json.dump({"name":"Recorrido Lonas P12","short_name":"Lonas P12","start_url":".","display":"standalone","background_color":"#c8102e","theme_color":"#c8102e","icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"}]},open('manifest.json','w'))
open('sw.js','w').write("""const C='lonas-p12-v7',F=['./','index.html','manifest.json','icon-192.png','xlsx.full.min.js','exceljs.min.js','jspdf.umd.min.js','jspdf.plugin.autotable.min.js'];
self.addEventListener('install',e=>e.waitUntil(caches.open(C).then(c=>c.addAll(F))));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x))))));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||!e.request.url.startsWith(self.location.origin))return;
e.respondWith(fetch(e.request).then(r=>{const c=r.clone();caches.open(C).then(x=>x.put(e.request,c));return r}).catch(()=>caches.match(e.request)))});
""")
from PIL import Image,ImageDraw
for s in (192,512):
    im=Image.new('RGB',(s,s),'#c8102e');dr=ImageDraw.Draw(im)
    dr.ellipse([s*.28,s*.15,s*.72,s*.59],fill='white');dr.polygon([(s*.3,s*.5),(s*.7,s*.5),(s*.5,s*.85)],fill='white');dr.ellipse([s*.42,s*.29,s*.58,s*.45],fill='#c8102e')
    im.save(f'icon-{s}.png')
print(len(recs),len(addr))
