from adapter import *

import random

# Clase abstracta ModoReproduccion
class ModoReproduccion:
    def reproducir_playlist(self, playlist, adapter):
        pass

# Clase concreta OrdenAleatorio
class OrdenAleatorio(ModoReproduccion):
    def reproducir_playlist(self, playlist, adapter):
        canciones_aleatorias = random.sample(playlist, len(playlist))
        for cancion in canciones_aleatorias:
            adapter.stream_music(cancion)

# Clase concreta OrdenNormal
class OrdenNormal(ModoReproduccion):
    def reproducir_playlist(self, playlist, adapter):
        for cancion in playlist:
            adapter.stream_music(cancion)

# Clase concreta RepetirTodos
class RepetirTodos(ModoReproduccion):
    def reproducir_playlist(self, playlist, adapter):
        while True:
            for cancion in playlist:
                adapter.stream_music(cancion)

# Clase concreta RepetirUnaPista
class RepetirUnaPista(ModoReproduccion):
    def reproducir_playlist(self, playlist, adapter):
        while True:
            adapter.stream_music(playlist[0])

# Adaptador para dispositivo Bluetooth
bluetooth_adapter = BluetoothAdapter()

# Adaptador para dispositivo HDMI
hdmi_adapter = HDMIAdapter()

# Adaptador para dispositivo USB
usb_adapter = USBAdapter()

# Modo de reproducción por defecto: orden normal
modo_reproduccion = OrdenNormal()

# Menú para seleccionar el modo de reproducción
while True:
    print("Selecciona el modo de reproducción:")
    print("")
    print("1. Orden aleatorio")
    print("2. Orden normal")
    print("3. Repetir todas las canciones")
    print("4. Repetir una pista")
    print("")
    opcion = input("Escribe el número de la opción: ")

    if opcion == "1":
        modo_reproduccion = OrdenAleatorio()
        break
    elif opcion == "2":
        modo_reproduccion = OrdenNormal()
        break
    elif opcion == "3":
        modo_reproduccion = RepetirTodos()
        break
    elif opcion == "4":
        modo_reproduccion = RepetirUnaPista()
        break
    else:
        print("Opción no válida")

# Reproducir la playlist en el modo seleccionado
modo_reproduccion.reproducir_playlist(canciones, bluetooth_adapter)
