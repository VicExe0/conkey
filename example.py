from typing import Optional, NoReturn

from conkey import KeyboardEngine, Event, Key

def mainloop( event: Event ) -> Optional[int]:
    if event.keyDown():
        if event.key == Key.ESCAPE:
            event.stop() # return -1
        
        else:
            print(f"{event.key=}, {event.frame=}, CTRL?: {event.ctrlDown()}, CAPS: {event.capsOn()}, SHIFT: {event.shiftDown()}")

    if event.frame % 30 == 0:
        print("0.5s")


if __name__ == "__main__":
    kbe = KeyboardEngine()

    kbe.start(mainloop)