import pytube


url = input("Ingrese url del video: ")
path = input("Ingrese carpeta de destino: ")

pytube.YouTube(url).streams.get_highest_resolution().download(path)

print("Video descargado!")
