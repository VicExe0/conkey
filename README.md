# conkey

Easy and simple console keyboard handler and render engine for Python console apps and games.

## Features

- Real-time keyboard input handling (including special keys)
- Runs a render loop at configurable FPS
- Thread-safe key event handling
- Supports key state checks (Ctrl, CapsLock, Shift)
- Easy to integrate for console games, menus, or interactive apps

## Installation

Copy the `conkey.py` module into your project.

## Usage

```python
from conkey import KeyboardEngine, Event, Key

def mainloop(event: Event):
    if event.keyDown():
        print(f"Key pressed: {event.key}")

    if event.key == Key.ESCAPE:
        return -1  # stops the engine

engine = KeyboardEngine()
engine.start(mainloop)
```

## Documentation

### KeyboardEngine

#### `start(callback: Callable, fps: int = 60, suspense: bool = True) -> NoReturn`

Starts the keyboard engine and main loop. Calls `callback` every frame with an `Event` object as a argument.

- `callback`: function accepting an `Event` parameter
- `fps`: frames per second (default 60)
- `suspense`: if True, blocks main thread until engine stops

#### `stop() -> None`

Stops the engine and joins threads.

---

### Event

Represents a keyboard event.

- `.key`: key pressed as a string or enum member
- `.lkey`: key pressed as a lowercase string or enum member
- `.ukey`: key pressed as a uppercase string or enum member
- `.frame`: current frame count
- `.ctrl`, `.shift`, `.caps`: booleans representing modifier key states
- `.keyDown() -> bool`: returns True if any key is pressed
- `.shiftDown() -> bool`: returns True if shift is pressed
- `.ctrlDown() -> bool`: returns True if ctrl is pressed
- `.capsOn() -> bool`: returns True if caps is on
- `.stop() -> NoReturn`: stop the handler

---

### Key Enum

Enumerates supported keys for safer comparisons.


### Callback

Should accept one argument.
When returns `-1` handler stops.