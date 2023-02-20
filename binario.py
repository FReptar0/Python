import serial

ser = serial.Serial('COM4', 9600)

while True:
    numBinario = ser.readline().decode().strip()
    numDecimal = int(numBinario, 2)
    ser.write(str(numDecimal).encode())
    print(numDecimal)
