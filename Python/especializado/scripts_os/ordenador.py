import os 
import shutil

#directorio de la carpeta a ordenar
DIRECTORY = "C:\\Users\\indatech\\Downloads"

#categorias que vamos a ordenar
CATEGORIES = {
  "images": [".jpg", ".jpeg", ".png", ".svg", "webp"],
  "videos": [".avi", ".mp4", ".mov"],
  "documents": [".doc", ".docx", ".pdf", ".xls", ".xlsx"],
  "audio": [".mp3", ".ogg", ".wav", ".amr"],
  "archives": [".zip", ".gz", ".tar"],
  "ejecutables": [".exe", ".msi"],
  "others": []
}

#recorremos las categorias para asegurarnos que las carpetas existen
for category in CATEGORIES:
  path_Route = os.path.join(DIRECTORY, category)
  if not os.path.exists(path_Route):
    #si no existe la carpeta la creamos
    os.mkdir(path_Route)
    
    
#Recorremos la carpeta seleccionada para categorizar todos sus archivos

for file in os.listdir(DIRECTORY):
  if os.path.isfile(os.path.join(DIRECTORY, file)):
    name, extension = os.path.splitext(file)
    extesion = extension.lower()
    for category, extensions in CATEGORIES.items():
      if extesion in extensions:
        origin = os.path.join(DIRECTORY, file)
        destination = os.path.join(DIRECTORY, category)
        shutil.move(origin, destination)
        break
      
#Eliminacion de archivos temporales
import glob

def clean_temp_files():
  temp_dirs = [
    "C:\\Users\\indatech\\AppData\\Local\\Temp",
    "C:\\Windows\\Temp",
    os.path.expanduser("~\\AppData\\Local\\Temp\\*")
  ]
  for temp_dir in temp_dirs:
    for file in glob.glob(temp_dir):
      try:
        if os.path.isfile(file):
          os.remove(file)
        elif os.path.isdir(file):
          shutil.rmtree(file)
      except Exception as e:
        print(f"Error al eliminar el archivo {file}: {e}")
        
clean_temp_files()

#Conversor de Imagenes
from PIL import Image

def convert_to(format ='webp', quality = 90):
  formats = [".jpg", ".jpeg", ".png", ".webp"]
  directory = "C:\\Users\\indatech\\Downloads\\images"
  
  for file in os.listdir(directory):
    name, extension = os.path.splitext(file)
    if extension.lower() in formats:
      origin = os.path.join(directory, file)
      destination = os.path.join(directory, f"{name}.{format}")
      try:
        image = Image.open(origin)
        image.save(destination, format=format.upper(), quality=quality)
        print(f"Imagen {file} convertida a {format} con calidad {quality}")
      except Exception as e:
        print(f"Error al convertir la imagen {file}: {e}")
        
convert_to()