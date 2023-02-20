import serial
import time
import datetime

# Crea una instancia de la conexión con Arduino
ser = serial.Serial('COM3', 9600)

while True:
    data = ser.readline().decode()
    current_time = datetime.datetime.now()
    print(data + "Dia y hora: " + current_time.strftime("%Y-%m-%d %H:%M:%S"))
