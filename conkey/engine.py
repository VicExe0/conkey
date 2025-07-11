from typing import Callable, NoReturn

from .event import Event
from .consts import ALLOWED, SPECIAL

import threading
import msvcrt
import time

def _getCharKey( key ) -> str:
    try:
        char = key.decode()

        if char in ALLOWED:
            return char
        
    except UnicodeDecodeError:
        pass

    return SPECIAL.get(key, None)


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

                key_name = SPECIAL.get(SKEY, None)

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
