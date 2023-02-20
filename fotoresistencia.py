import serial

ser = serial.Serial('COM4',9600)
cont = 0

while True:
    lecture = ser.readline().decode()
    print(lecture)
    with open('C:\\Users\\sansc\\Desktop\\UTEZ\\5°\\IOT\\Python\\Datos.txt', 'a') as f:
        f.write(lecture) 
        cont = cont + 1