import os
import sys
import serial
import time

arduino = serial.Serial()
arduino.port = "/dev/ttyACM1"
arduino.baudrate = 9600
arduino.bytesize=serial.EIGHTBITS
arduino.parity=serial.PARITY_NONE
arduino.stopbits=serial.STOPBITS_ONE
arduino.timeout=1
arduino.xonxoff=False
arduino.rtscts=False
arduino.dsrdtr=False
arduino.writeTimeout=None

def connect():
    print("opening conection with arduino..")
    arduino.open()
    time.sleep(2)

def sendData(data):
    if arduino.is_open:
        print("sending data {}".format(data))
        arduino.write(data.encode())    

def close(data):
    print("closing conection with arduino..")
    arduino.close()

def testing():
    print("turning on led...")    
    arduino.write("on".encode())

connect()