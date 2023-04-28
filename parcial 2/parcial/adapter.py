# Clase abstracta MediaAdapter
class MediaAdapter:
    def stream_music(self, cancion):
        pass

# Clase concreta BluetoothAdapter
class BluetoothAdapter(MediaAdapter):
    def stream_music(self, cancion):
        print(f"Reproduciendo '{cancion.nombre}' en dispositivo Bluetooth...")

# Clase concreta HDMIAdapter
class HDMIAdapter(MediaAdapter):
    def stream_music(self, cancion):
        print(f"Reproduciendo '{cancion.nombre}' en dispositivo HDMI...")

# Clase concreta USBAdapter
class USBAdapter(MediaAdapter):
    def stream_music(self, cancion):
        print(f"Reproduciendo '{cancion.nombre}' en dispositivo USB...")

# Clase Cancion
class Cancion:
    def __init__(self, artista, nombre, genero, duracion):
        self.artista = artista
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion

# Función para cargar datos
def load_csv_py(filename):
    dataset=[]
    with open(filename, encoding='utf8') as f:
        for linea in f:
            data_line = linea.strip().split(";")
            cancion = Cancion(data_line[0], data_line[1], data_line[2], data_line[3])
            dataset.append(cancion)
    return dataset

# Main
archivo = input("Nombre del archivo de datos?: ")
canciones = load_csv_py(archivo)

# Adaptador para dispositivo Bluetooth
bluetooth_adapter = BluetoothAdapter()

# Adaptador para dispositivo HDMI
hdmi_adapter = HDMIAdapter()

# Adaptador para dispositivo USB
usb_adapter = USBAdapter()

for cancion in canciones:
    # Seleccionar el medio por el que se quiere reproducir la canción
    medio = input(f"¿Cómo quieres reproducir '{cancion.nombre}'? (bluetooth/hdmi/usb): ")

    # Crear el adaptador correspondiente al medio seleccionado
    if medio == "bluetooth":
        adapter = bluetooth_adapter
    elif medio == "hdmi":
        adapter = hdmi_adapter
    elif medio == "usb":
        adapter = usb_adapter
    else:
        print("Medio no válido")
        continue

    # Reproducir la canción usando el adaptador correspondiente
    adapter.stream_music(cancion)
