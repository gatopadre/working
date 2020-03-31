import arduinoController

onBoardLedOn = "on"
onBoardLedOff = "off"

def turnOnBoardLed():
    print("llego la peticion de encender el led")
    arduinoController.sendData(onBoardLedOn)
    pass

def turnOffBoardLed():
    print("llego la peticion de apagar el led")
    arduinoController.sendData(onBoardLedOff)
    pass
