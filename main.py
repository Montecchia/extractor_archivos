import os
import shutil

cantidad_movida = 0 # Contador
directorio = input("Ingrese el directorio base: ")
if not os.path.exists(directorio):
    exit("No existe el directorio")
extension = input("Ingrese la extension de los archivos a sacar: ")  # Ej: ".mkv" o "iso"
if not extension.startswith("."):  # Corrección en caso de no haber incluído el punto en la extensión
    extension = "." + extension

print("Directorio correcto, moviendo...")
carpetas = os.listdir(directorio)  # Ubica todos los archivos en la carpeta base
for carpeta in carpetas:
    posible_carpeta = directorio+"/"+carpeta  # Obtiene el path de los archivos
    if os.path.isdir(posible_carpeta):  # Si son una carpeta procede a buscar los archivos a sacar
        print(posible_carpeta)
        archivos = os.listdir(posible_carpeta)  # Ubica los posibles archivos a sacar
        for archivo in archivos:
            if archivo.endswith(extension):  # Si tienen la extensión deseada se procede
                origen = posible_carpeta + "/" + archivo
                destino = directorio + "/" + archivo
                print("Moviendo", archivo, "a", directorio)
                shutil.move(origen, destino)  # Se mueven a la carpeta base
                cantidad_movida += 1

print("Se movieron " + str(cantidad_movida) + " archivos " + extension + " a " + directorio)  # Informa cantidad movida
