import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin("a:0:i")

print("apply hrm now")

list1 = []
for i in range(0, 100):
    analog_value = analog_input.read()
    time.sleep(0.1)
    list1.append(analog_value)

del list1[0]
print(list1)
average = sum(list1) / len(list1)
print(average)

if 0.35 <= average and average <= 0.5:
    board.digital[13].write(1)
    time.sleep(4)
    board.digital[13].write(0)

#
