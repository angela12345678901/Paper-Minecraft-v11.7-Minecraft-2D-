import os
import shutil
from pathlib import Path

def organizar_carpeta(ruta_objetivo):
    # Diccionario con las reglas de clasificación
    CATEGORIAS = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Comprimidos": [".zip", ".rar", ".tar", ".gz"],
        "Ejecutables": [".exe", ".msi", ".dmg", ".sh"]
    }
    
    ruta = Path(ruta_objetivo)
    if not ruta.exists():
        return "La ruta especificada no existe."

    for archivo in ruta.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()
            encontrado = False
            
            # Buscar a qué categoría pertenece el archivo
            for categoria, extensiones in CATEGORIAS.items():
                if extension in extensiones:
                    carpeta_destino = ruta / categoria
                    carpeta_destino.mkdir(exist_ok=True) # Crea la carpeta si no existe
                    shutil.move(str(archivo), str(carpeta_destino / archivo.name))
                    encontrado = True
                    break
            
            # Si tiene una extensión desconocida, va a 'Otros'
            if not encontrado:
                carpeta_otros = ruta / "Otros"
                carpeta_otros.mkdir(exist_ok=True)
                shutil.move(str(archivo), str(carpeta_otros / archivo.name))
                
    return "¡Carpeta organizada con éxito!"

# Ejemplo de uso (reemplaza con tu ruta real):
# print(organizar_carpeta("C:/Usuarios/TuUsuario/Downloads"))
