import serial

ser = serial.Serial('COM4', 9600)

while True:
    write = input("Escribe algo: ")
    ser.write(write.encode())
    