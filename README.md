# Recorrido Lonas P12

App web (PWA) para el recorrido de instalación de lonas y pendones.

## Publicar en GitHub Pages
1. Sube TODOS estos archivos a la raíz de un repositorio: `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `xlsx.full.min.js`.
2. Settings → Pages → Deploy from a branch → `main` / `(root)` → Save.
3. Abre `https://TU-USUARIO.github.io/NOMBRE-REPO/` en el celular (HTTPS, necesario para el GPS).

## Cargar tus datos desde Excel
1. Completa `Plantilla_Recorrido.xlsx` (hoja "Recorrido"; las instrucciones están en la otra hoja).
2. En la app: **📥 Cargar Excel**. La app reemplaza los datos y crea rutas, tiendas, mapa y orden.
3. **📤 Bajar Excel** exporta los datos actuales (con las coordenadas ya guardadas) para editarlos y volver a cargarlos.

`build.py`, `template.html` y `make_template.py` regeneran la app y la plantilla con los datos originales.
