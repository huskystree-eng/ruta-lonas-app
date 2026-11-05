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

## Guardar el informe en tu carpeta de GitHub
Pulsa **⚙ GitHub** (una sola vez) e indica usuario, repositorio, rama y carpeta (por defecto `evidencias`), más un token fine-grained de GitHub limitado a ese repositorio con permiso *Contents: Read and write*. Desde entonces, **📸 Informe con fotos** sube el Excel directo al repositorio (no al celular); en tu computadora haz `git pull` y aparece en esa carpeta. Si falla la subida, se descarga/comparte como antes.
Ojo: si el repositorio es público, las fotos también lo serán.
