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
