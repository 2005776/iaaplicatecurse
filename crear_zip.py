from zipfile import ZipFile
import os

# Crear carpeta
folder_name = "curso_ia_web"
os.makedirs(folder_name, exist_ok=True)

# Contenido de index.html
html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Curso: Aprende IA para Programar</title>
  <style>
    /* estilos aquí... */
  </style>
</head>
<body>
  <!-- contenido HTML del curso aquí... -->
  <script>
    // código JavaScript aquí...
  </script>
</body>
</html>
'''

# Guardar index.html
with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

# Crear ZIP
with ZipFile(f"{folder_name}.zip", "w") as zipf:
    zipf.write(os.path.join(folder_name, "index.html"), arcname="index.html")

print("✅ ZIP creado: curso_ia_web.zip")
