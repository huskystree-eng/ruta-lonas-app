# Recorrido Lonas P12

## Publicar en GitHub Pages
1. Sube a la raíz del repositorio: `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `xlsx.full.min.js` y `exceljs.min.js`.
2. Settings → Pages → Deploy from a branch → `main` / `(root)`.
3. Abre `https://TU-USUARIO.github.io/NOMBRE-REPO/` en el celular.

## Datos desde Excel
Completa `Plantilla_Recorrido.xlsx` (hoja "Recorrido") y en la app pulsa **📥 Cargar Excel**.
La app arma rutas, tiendas, mapa, qué hacer, material y promoción. **📤 Bajar Excel** exporta lo actual.

Regenerar: `python3 build.py` (app) y `python3 make_template.py` (plantilla).

## Fotos e informe al cliente
En cada espacio: 📷 Antes / 📷 Después (abre la cámara, pone fecha, hora, tienda y GPS sobre la foto). Al tomar la foto "Después" el espacio se marca como hecho. **📸 Informe con fotos** genera un Excel con las fotos incrustadas y lo comparte (WhatsApp/correo) o lo descarga.

## Guardar el informe directo en GitHub
⚙️ GitHub → repositorio (usuario/repo, de preferencia PRIVADO), carpeta (evidencias) y token fine-grained con permiso Contents: Read and write solo para ese repositorio. Después, 📸 Informe con fotos sube el Excel a esa carpeta.

## Modo simple (empleados) y modo completo (administrador)
La app abre en **modo simple**: elegir ruta → una tienda a la vez → qué colocar → 📷 Antes → 📷 Después → siguiente. El administrador entra con "Administrador (modo completo)".
En modo completo: **✏️ Editar rutas** (ordenar tiendas, mover/quitar/agregar tiendas, crear/renombrar/borrar/ordenar rutas, tienda nueva, pieza nueva) y **🖨 PDF** por ruta o de todas, listo para imprimir (carta horizontal, casilla de hecho y notas).
Los cambios del editor se guardan en el celular. Para reiniciar: ♻ Originales.
