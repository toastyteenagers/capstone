import pyfirmata
import time
board = pyfirmata.Arduino("/dev/ttyACM0")
it = pyfirmata.util.Iterator(board)
it.start()
analog = board.get_pin("a:0:i")

def openDoor():
    board.digital[13].write(1)


def closeDoor():
    board.digital[13].write(0)

async def OpenFor5():
    openDoor()
    sleep(5)
    closeDoor()
def toggle():
    if isDoorOpen == False:
        openDoor()
    else:
        closeDoor()