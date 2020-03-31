from ../controllers import lightsController
import time

print("Opciones:")
print("led on - enciende led de la placa arduino")
print("led off - apaga led de la placa arduino")
print("salir - cierra el programa")
print("Ingrese una opcion:")

option = input()
print("La opcion ingresada fue {}".format(option))
while option != "salir":
    if option == "led on":
        lightsController.turnOnBoardLed()
    if option == "led off":
        lightsController.turnOffOnBoardLed()
    option = input("ingrese una opcion:")