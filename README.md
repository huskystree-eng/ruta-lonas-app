# Recorrido Lonas P12

App web (PWA) para hacer el recorrido de instalación de lonas y pendones.

## Publicar en GitHub Pages
1. Crea un repositorio nuevo en GitHub y sube estos archivos: `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`.
2. En el repositorio: Settings → Pages → Source: "Deploy from a branch" → Branch `main` / carpeta `/ (root)` → Save.
3. Abre `https://TU-USUARIO.github.io/NOMBRE-REPO/` en el celular (con HTTPS el GPS funciona).
4. En el celular: menú del navegador → "Agregar a pantalla de inicio".

El avance (checks y notas) se guarda en el propio celular. `build.py` y `template.html` sirven para regenerar `index.html` si cambian los datos.
