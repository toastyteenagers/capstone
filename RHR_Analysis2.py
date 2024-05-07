# from the information found in this paper: https://www.researchgate.net/figure/Distribution-of-average-daily-resting-heart-rates-The-average-daily-RHR-for-57-836_fig2_339061433
print("I'm being imported2")
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

class RHR_Analysis_LIB:
    def __init__(self):
        self.mean = 65.5
        self.std_dev = 3.10
        self.allowable_deviation = 10

        self.isDoorOpen = False

        self.currSample = 0  # this is an index variable, the np array should have arr[currSample] = currentIntesnity
        self.sampleRate = 1 / (.02)  # samples every 2ms, this is the sample rate in hz
        self.samplingTime = 10
        self.totalNeededSamples = 5000  # amount needed for analysis

        self.baud = 9600
        # analog = Serial.Serial(port="/dev/ttyACM0",baudrate=baud,timeout=1)
        self.board = pyfirmata.Arduino("/dev/ttyACM0")
        self.board.digital[13].mode = pyfirmata.OUTPUT
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.analog = self.board.get_pin("a:0:i")


    ## to read from analog pin, use analog.read()

    # digital13 = digitalio.DigitalInOut(board.D13)
    # digital13.direction = digitalio.Direction.OUTPUT

    # return true if the user is 3+ deviatons away from the mean set from their resting rate.
    def analyze(self, rhr, observedHR):
        std_deviations_away = abs(observedHR - rhr) / self.std_dev
        return std_deviations_away > self.allowable_deviation


    # this class will analyze the users' resting heart rate by using a statistical model derived


    def clean(self, currString):
        reconstructedInt = ""
        for char in str(currString):
            if char.isdigit():
                reconstructedInt += char
        return int(reconstructedInt) if reconstructedInt else 0

    #async
    def sample(self):
        print("Place your hand on the sensor")
        self.currSample = 0
        beatList = []
        lastValue = -1
        while self.currSample < self.totalNeededSamples:
            start_time = time.time()  # Start timing before the loop body

            currString = self.analog.read()
            if currString is None:
                continue  # Skip None readings which might occur initially

            currIntensity = self.clean(currString)
            beatList.append(currIntensity)
            self.currSample += 1

            # Uncomment below for debugging or progress update purposes
            if self.currSample % 100 == 0:
                print(f"Sampling {100 * self.currSample / self.totalNeededSamples:.2f}% done")
            #     print(currIntensity)

            # Calculate elapsed time and adjust sleep time
            elapsed_time = time.time() - start_time
            sleep_time = max(0.002 - elapsed_time, 0)  # Ensure sleep_time is not negative

            time.sleep(sleep_time)  # Sleep the adjusted amount of time
        self.board.exit()
        return beatList

    #async
    def analysis(self, beatList):
        if len(beatList) == 0:
            return 85.12
        beatList2 = [point for point in beatList if 200 < point < 800]
        indexList = list(range(1, len(beatList2) + 1))
        try:
            wd, m = hp.process(np.asarray(beatList2), sample_rate=self.sampleRate)
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

    def isOpen(self):
        return self.board.sp.isOpen()

    def fixThing(self):
        if not self.isOpen():
            self.board.sp.open()

    def openDoor(self):
        #halt analog readings
        #then write to the pin
        #then resume
        #board.iterate()
        self.fixThing()
        self.board.digital[13].write(1)


    def closeDoor(self):
        self.fixThing()
        self.board.digital[13].write(0)

    def OpenFor5(self):
        self.openDoor()
        sleep(5)
        self.closeDoor()

    def toggle(self):
        if self.isDoorOpen == False:
            self.openDoor()
        else:
            self.closeDoor()
        self.isDoorOpen = not(self.isDoorOpen)
