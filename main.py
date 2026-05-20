import os
import shutil

# Ruta de la carpeta que quieres organizar
ruta = input("Ingresa la ruta de la carpeta que deseas organizar: ")

# Tipos de archivos
extensiones = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documentos": [".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv"],
    "Musica": [".mp3"],
    "Archivos ZIP": [".zip", ".rar"]
}

# Crear carpetas si no existen
for carpeta in extensiones.keys():
    os.makedirs(os.path.join(ruta, carpeta), exist_ok=True)

# Recorrer archivos
for archivo in os.listdir(ruta):
    archivo_ruta = os.path.join(ruta, archivo)

    # Verificar si es archivo
    if os.path.isfile(archivo_ruta):

        # Obtener extensión
        _, extension = os.path.splitext(archivo)

        # Buscar carpeta correspondiente
        for carpeta, extensiones_lista in extensiones.items():

            if extension.lower() in extensiones_lista:

                destino = os.path.join(ruta, carpeta, archivo)

                shutil.move(archivo_ruta, destino)

                print(f"Movido: {archivo} → {carpeta}")

print("Organización completada.")