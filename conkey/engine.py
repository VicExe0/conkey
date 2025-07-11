from typing import Callable, NoReturn

from .event import Event

import threading
import msvcrt
import time

__ALLOWED = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~ \b"
__SPECIAL = {
    b'\r': "ENTER",
    b'\x08': "BACKSPACE",
    b'\t': "TAB",
    b'\x1b': "ESCAPE",
    b' ': "SPACE",
    b'\xe0': "PREFIX",
    b'H': "ARROW_UP",
    b'P': "ARROW_DOWN",
    b'K': "ARROW_LEFT",
    b'M': "ARROW_RIGHT",
    b'R': "INSERT",
    b'S': "DELETE",
    b'G': "HOME",
    b'O': "END",
    b'I': "PAGE_UP",
    b'Q': "PAGE_DOWN",
    b'\x00': "PREFIX_FUNC",
    b';': "F1",
    b'<': "F2",
    b'=': "F3",
    b'>': "F4",
    b'?': "F5",
    b'@': "F6",
    b'A': "F7",
    b'B': "F8",
    b'C': "F9",
    b'D': "F10",
    b'\x85': "F11",
    b'\x86': "F12",
}

# CTRL + ... combinations
for i in range(1, 27):
    __SPECIAL[bytes([i])] = f"CTRL_{chr(64 + i)}"

# Not supported:
# CTRL + [ (works as ESCAPE key)
# CTRL + S (ignored)
# CTRL + C (ignored)
# CTRL + H (works as BACKSPACE key)

def _getCharKey( key ) -> str:
    try:
        char = key.decode()

        if char in __ALLOWED:
            return char
        
    except UnicodeDecodeError:
        pass

    return __SPECIAL.get(key, None)


class KeyboardEngine:
    def __init__( self ) -> None:
        self.key = None
        self.lock = threading.Lock()

        self.callback = None
        self.running = False

        self.input_thread = None
        self.main_thread = None


    def start( self, callback: Callable, fps: int = 60, suspense: bool = True ) -> NoReturn:
        """
        Start the engine.

        Runs the callback function at the specified frames per second (fps).
        
        Args:
            callback (Callable): Function called every frame with event data.
            fps (int, optional): Frames per second to run the loop. Defaults to 60.
            suspense (bool, optional): If True, blocks main thread until stopped. Defaults to True.
        """
        self.callback = callback
        self.running = True

        self.input_thread = threading.Thread(target=self.__inputHandler)
        self.main_thread = threading.Thread(target=self.__mainLoop, args=(fps,))

        self.input_thread.start()
        self.main_thread.start()


        while self.running and suspense:
            try:
                time.sleep(0.01)

            except KeyboardInterrupt:
                pass


    def stop( self ) -> None:
        "Stop the engine."
        self.running = False

        if threading.current_thread() != self.input_thread:
            self.input_thread.join()

        if threading.current_thread() != self.main_thread:
            self.main_thread.join()


    def __inputHandler( self ) -> NoReturn:
        while self.running:
            if not msvcrt.kbhit():
                time.sleep(0.01)
                continue

            KEY = msvcrt.getch()

            if KEY in ( b'\x00', b'\xe0' ):
                SKEY = msvcrt.getch()

                key_name = __SPECIAL.get(SKEY, None)

                with self.lock:
                    self.key = key_name

            else:
                char_key = _getCharKey(KEY)

                with self.lock:
                    self.key = char_key


    def __mainLoop( self, fps: int ) -> NoReturn:
        frame_duration = 1 / fps
        frame = 0

        while self.running:
            start = time.perf_counter()

            frame += 1

            with self.lock:
                key = self.key
                self.key = None

            response = self.callback(Event(key, frame, self.stop))

            if frame >= fps:
                frame = 0

            if response == -1:
                self.stop()

            elapsed = time.perf_counter() - start
            time.sleep(max(0, frame_duration - elapsed))


