import serial, time

ser = serial.Serial('COM3', 9600)

while 1:
    f = open('data.txt','w')
    data = ser.readline()
    f.write(data)
    f.close()
    time.sleep(1)

    
  