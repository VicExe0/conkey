from typing import NoReturn, Callable
import ctypes

class Event:
    def __init__( self, key: str, frame: int, _stop_func: Callable ) -> None:
        self.key = key
        self.frame = frame
        self.letter = len(key) == 1 if key else False

        self.lkey = key.lower() if key else None
        self.ukey = key.upper() if key else None

        self.ctrl = bool(ctypes.windll.user32.GetKeyState(0x11) & 0x8000)   # 0x11 - VK_CONTROL
        self.caps = bool(ctypes.windll.user32.GetKeyState(0x14) & 1)        # 0x14 - VK_CAPITAL
        self.shift = bool(ctypes.windll.user32.GetKeyState(0x10) & 0x8000)  # 0x10 - VK_SHIFT

        self._stop_func = _stop_func

    def keyDown( self ) -> bool:
        "Is any key pressed. ( True / False )"
        return self.key is not None
    
    def shiftDown( self ) -> bool:
        "Is SHIFT pressed. ( True / False )"
        return self.shift

    def ctrlDown (self ) -> bool:
        "Is CTRL pressed. ( True / False )"
        return self.ctrl

    def capsOn( self ) -> bool:
        "Is CAPS on. ( True / False )"
        return self.caps
    
    def stop( self ) -> NoReturn:
        "Stops the engine."
        self._stop_func()