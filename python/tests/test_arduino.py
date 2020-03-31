import os
import sys
import serial
import serial
import time

arduino = serial.Serial(
    port = "/dev/ttyACM1",
    baudrate = 9600,
    bytesize = serial.EIGHTBITS, 
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE, 
    timeout = 1,
    xonxoff = False,
    rtscts = False,
    dsrdtr = False,
    writeTimeout = 2
    )

encender = "led on"

# ayuda a que arduino no se bloquee
time.sleep(2)
arduino.write(b"on")
time.sleep(2)
arduino.write(b"off")
time.sleep(2)
arduino.write(encender.encode())
time.sleep(2)
arduino.write("off".encode())
arduino.close()