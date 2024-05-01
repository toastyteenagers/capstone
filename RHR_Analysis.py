# from the information found in this paper: https://www.researchgate.net/figure/Distribution-of-average-daily-resting-heart-rates-The-average-daily-RHR-for-57-836_fig2_339061433
print("I'm being imported")
import UserFields
import asyncio
import concurrent.futures
import serial as Serial
import heartpy as hp
import time
import pyfirmata

import numpy as np
import matplotlib.pyplot as plt

from time import sleep

mean = 65.5
std_dev = 3.10
allowable_deviation = 3

isDoorOpen = False

currSample = 0  # this is an index variable, the np array should have arr[currSample] = currentIntesnity
sampleRate = 1 / (.02)  # samples every 2ms, this is the sample rate in hz
samplingTime = 10
totalNeededSamples = 5000  # amount needed for analysis

baud = 9600
# analog = Serial.Serial(port="/dev/ttyACM0",baudrate=baud,timeout=1)
board = pyfirmata.Arduino("/dev/ttyACM0")
board.digital[13].mode = pyfirmata.OUTPUT
it = pyfirmata.util.Iterator(board)
it.start()
analog = board.get_pin("a:0:i")


## to read from analog pin, use analog.read()

# digital13 = digitalio.DigitalInOut(board.D13)
# digital13.direction = digitalio.Direction.OUTPUT

# return true if the user is 3+ deviatons away from the mean set from their resting rate.
def analyze(userField, observedHR):
    std_deviations_away = abs(observedHR - userField.get_rhr()) / std_dev
    return std_deviations_away > allowable_deviation


# this class will analyze the users' resting heart rate by using a statistical model derived


def clean(currString):
    reconstructedInt = ""
    for char in str(currString):
        if char.isdigit():
            reconstructedInt += char
    return int(reconstructedInt) if reconstructedInt else 0


async def sample():
    print("Place your hand on the sensor")
    currSample = 0
    beatList = []
    lastValue = -1
    while currSample < totalNeededSamples:
        start_time = time.time()  # Start timing before the loop body

        currString = analog.read()
        if currString is None:
            continue  # Skip None readings which might occur initially

        currIntensity = clean(currString)
        beatList.append(currIntensity)
        currSample += 1

        # Uncomment below for debugging or progress update purposes
        if currSample % 100 == 0:
            print(f"Sampling {100 * currSample / totalNeededSamples:.2f}% done")
        #     print(currIntensity)

        # Calculate elapsed time and adjust sleep time
        elapsed_time = time.time() - start_time
        sleep_time = max(0.002 - elapsed_time, 0)  # Ensure sleep_time is not negative

        time.sleep(sleep_time)  # Sleep the adjusted amount of time
    board.exit()
    return beatList


async def analysis(beatList):
    beatList2 = [point for point in beatList if 200 < point < 800]
    indexList = list(range(1, len(beatList2) + 1))
    try:
        wd, m = hp.process(np.asarray(beatList2), sample_rate=sampleRate)
        for measure, value in m.items():
            print(f'{measure}: {value}')
    except Exception as e:
        print(f"Couldn't analyze! Error: {e}")
        return 85.12
    return m["bpm"]


# def toggle():
#    #also do the opening/closing (or just call whatever does it)
#    while True:
#        digital13.value = True
#        time.sleep(8)
#        digital13.value = False
#        time.sleep(8)




async def main():
    pass


if __name__ == '__main__':
    asyncio.run(main())
    
import time

def openDoor():
    global board
    #halt analog readings
    #then write to the pin
    #then resume
    #board.iterate()
    board.digital[13].write(1)


def closeDoor():
    global board
    board.digital[13].write(0)

def OpenFor5():
    openDoor()
    sleep(5)
    closeDoor()

def toggle():
    if isDoorOpen == False:
        openDoor()
    else:
        closeDoor()
    isDoorOpen = not(isDoorOpen)
