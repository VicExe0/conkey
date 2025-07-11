from enum import StrEnum

class Key(StrEnum):
    ENTER = "ENTER"
    BACKSPACE = "BACKSPACE"
    TAB = "TAB"
    ESCAPE = "ESCAPE"
    SPACE = "SPACE"
    PREFIX = "PREFIX"
    ARROW_UP = "ARROW_UP"
    ARROW_DOWN = "ARROW_DOWN"
    ARROW_LEFT = "ARROW_LEFT"
    ARROW_RIGHT = "ARROW_RIGHT"
    INSERT = "INSERT"
    DELETE = "DELETE"
    HOME = "HOME"
    END = "END"
    PAGE_UP = "PAGE_UP"
    PAGE_DOWN = "PAGE_DOWN"
    PREFIX_FUNC = "PREFIX_FUNC"
    
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    F10 = "F10"
    F11 = "F11"
    F12 = "F12"

    LOWER_A = "a"
    LOWER_B = "b"
    LOWER_C = "c"
    LOWER_D = "d"
    LOWER_E = "e"
    LOWER_F = "f"
    LOWER_G = "g"
    LOWER_H = "h"
    LOWER_I = "i"
    LOWER_J = "j"
    LOWER_K = "k"
    LOWER_L = "l"
    LOWER_M = "m"
    LOWER_N = "n"
    LOWER_O = "o"
    LOWER_P = "p"
    LOWER_Q = "q"
    LOWER_R = "r"
    LOWER_S = "s"
    LOWER_T = "t"
    LOWER_U = "u"
    LOWER_V = "v"
    LOWER_W = "w"
    LOWER_X = "x"
    LOWER_Y = "y"
    LOWER_Z = "z"

    UPPER_A = "A"
    UPPER_B = "B"
    UPPER_C = "C"
    UPPER_D = "D"
    UPPER_E = "E"
    UPPER_F = "F"
    UPPER_G = "G"
    UPPER_H = "H"
    UPPER_I = "I"
    UPPER_J = "J"
    UPPER_K = "K"
    UPPER_L = "L"
    UPPER_M = "M"
    UPPER_N = "N"
    UPPER_O = "O"
    UPPER_P = "P"
    UPPER_Q = "Q"
    UPPER_R = "R"
    UPPER_S = "S"
    UPPER_T = "T"
    UPPER_U = "U"
    UPPER_V = "V"
    UPPER_W = "W"
    UPPER_X = "X"
    UPPER_Y = "Y"
    UPPER_Z = "Z"

    DIGIT_0 = "0"
    DIGIT_1 = "1"
    DIGIT_2 = "2"
    DIGIT_3 = "3"
    DIGIT_4 = "4"
    DIGIT_5 = "5"
    DIGIT_6 = "6"
    DIGIT_7 = "7"
    DIGIT_8 = "8"
    DIGIT_9 = "9"

    EXCLAMATION = "!"
    AT = "@"
    HASH = "#"
    DOLLAR = "$"
    PERCENT = "%"
    CARET = "^"
    AMPERSAND = "&"
    ASTERISK = "*"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    DASH = "-"
    UNDERSCORE = "_"
    EQUAL = "="
    PLUS = "+"
    LEFT_BRACKET = "["
    RIGHT_BRACKET = "]"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    SEMICOLON = ";"
    COLON = ":"
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = "\""
    COMMA = ","
    DOT = "."
    LESS = "<"
    GREATER = ">"
    SLASH = "/"
    QUESTION = "?"
    BACKSLASH = "\\"
    PIPE = "|"
    BACKTICK = "`"
    TILDE = "~"

ALLOWED = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~ \b"
SPECIAL = {
    b'\r': Key.ENTER,
    b'\x08': Key.BACKSPACE,
    b'\t': Key.TAB,
    b'\x1b': Key.ESCAPE,
    b' ': Key.SPACE,
    b'\xe0': Key.PREFIX,
    b'H': Key.ARROW_UP,
    b'P': Key.ARROW_DOWN,
    b'K': Key.ARROW_LEFT,
    b'M': Key.ARROW_RIGHT,
    b'R': Key.INSERT,
    b'S': Key.DELETE,
    b'G': Key.HOME,
    b'O': Key.END,
    b'I': Key.PAGE_UP,
    b'Q': Key.PAGE_DOWN,
    b'\x00': Key.PREFIX_FUNC,
    b';': Key.F1,
    b'<': Key.F2,
    b'=': Key.F3,
    b'>': Key.F4,
    b'?': Key.F5,
    b'@': Key.F6,
    b'A': Key.F7,
    b'B': Key.F8,
    b'C': Key.F9,
    b'D': Key.F10,
    b'\x85': Key.F11, # Will probably be ignored due to fullscreen mode toggling on console
    b'\x86': Key.F12,
}

# CTRL + ... combinations
for i in range(1, 27):
    SPECIAL[bytes([i])] = f"CTRL_{chr(64 + i)}"

# Not supported:
# CTRL + [ (works as ESCAPE key)
# CTRL + S (ignored)
# CTRL + C (ignored)
# CTRL + V (could be ignored)
# CTRL + H (works as BACKSPACE key)