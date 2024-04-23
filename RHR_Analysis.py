# from the information found in this paper: https://www.researchgate.net/figure/Distribution-of-average-daily-resting-heart-rates-The-average-daily-RHR-for-57-836_fig2_339061433

import UserFields
import asyncio
import concurrent.futures
import serial as Serial
import heartpy as hp
import time
import pyfirmata

import numpy as np
import matplotlib.pyplot as plt

mean = 65.5
std_dev = 3.10
allowable_deviation = 3

isDoorOpen = False

currSample = 0 # this is an index variable, the np array should have arr[currSample] = currentIntesnity
sampleRate = 1/(.02)  # samples every 2ms, this is the sample rate in hz
samplingTime = 50 
totalNeededSamples = samplingTime * sampleRate  # amount needed for analysis

baud = 9600
#analog = Serial.Serial(port="/dev/ttyACM0",baudrate=baud,timeout=1)
board = pyfirmata.Arduino("/dev/ttyACM0")
it = pyfirmata.util.Iterator(board)
it.start()
analog = board.get_pin("a:0:i")

## to read from analog pin, use analog.read()

#digital13 = digitalio.DigitalInOut(board.D13)
#digital13.direction = digitalio.Direction.OUTPUT

#return true if the user is 3+ deviatons away from the mean set from their resting rate.
def analyze(userField,observedHR):
    std_deviations_away = abs(observedHR-userField.get_rhr()) / std_dev
    return std_deviations_away > allowable_deviation

# this class will analyze the users' resting heart rate by using a statistical model derived


def clean(currString):
    reconstructedInt = ""
    for char in str(currString):
        if char.isdigit():
            reconstructedInt += char
    return int(reconstructedInt) if reconstructedInt else 0

async def sample():
    print("place hand on hrm")
    currSample = 0
    beatList = []
    with concurrent.futures.ThreadPoolExecutor() as pool:
        while len(beatList) < totalNeededSamples:
            # Replace analog.readline() with your actual blocking call
            currString = await asyncio.get_event_loop().run_in_executor(pool, analog.readline())
            currIntensity = clean(currString)
            currSample += 1
            if currSample % 100 == 0:
                print(f"sampling {100*currSample/totalNeededSamples}% done")
            beatList.append(currIntensity)
    return beatList

async def analysis(beatList):
    beatList2 = [point for point in beatList if 200 < point < 800]
    indexList = list(range(1, len(beatList2) + 1))
    plt.plot(indexList, beatList2)
    try:
        wd, m = hp.process(np.asarray(beatList2), sample_rate=sampleRate)
        for measure, value in m.items():
            print(f'{measure}: {value}')
    except Exception as e:
        print(f"Couldn't analyze! Error: {e}")
    plt.show()

#def toggle():
#    #also do the opening/closing (or just call whatever does it)
#    while True:
#        digital13.value = True
#        time.sleep(8)
#        digital13.value = False
#        time.sleep(8)
    
def openDoor():
    board.digital[13].write(1)

def closeDoor():
    board.digital[13].write(0)

def toggle():
    if isDoorOpen == False:
        openDoor()
    else:
        closeDoor()

async def main():
    beatList = await sample()
    await analysis(beatList)
    openDoor()
    time.sleep(8)
    closeDoor()


if __name__ == '__main__':
    asyncio.run(main())
