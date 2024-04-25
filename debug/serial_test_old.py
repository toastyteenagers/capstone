import serial

try:
    arduino = serial.Serial("/dev/ttyACM0", timeout=1)
except:
    print("check port")

rawdata = []
count = 0

while count < 3:
    rawdata.append(str(arduino.readline()))
    count += 1

print(rawdata)

