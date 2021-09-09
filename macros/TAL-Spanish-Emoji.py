# MACROPAD Hotkeys example: TAL Español & Emoji

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'español & emoji', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x250000, '~n', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, 
            Keycode.KEYPAD_FOUR, -Keycode.KEYPAD_FOUR,
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            -Keycode.ALT]),
        (0x250025, "'a", [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO,
            Keycode.KEYPAD_FIVE, -Keycode.KEYPAD_FIVE, 
            -Keycode.ALT]),
        (0x002525, '?', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            Keycode.KEYPAD_NINE, -Keycode.KEYPAD_NINE,
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            -Keycode.ALT]),
        # 2nd row ----------
        (0x250000, '~N', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO,
            Keycode.KEYPAD_NINE, -Keycode.KEYPAD_NINE, 
            -Keycode.ALT]),
        (0x250025, "'A", [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            Keycode.KEYPAD_NINE, -Keycode.KEYPAD_NINE,
            Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE, 
            -Keycode.ALT]),
        (0x002525, '!', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            Keycode.KEYPAD_SIX, -Keycode.KEYPAD_SIX,
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            -Keycode.ALT]),
        # 3rd row ----------
        (0x202020, 'ohms', [Keycode.ALT, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, 
            Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE,
            Keycode.KEYPAD_FOUR, -Keycode.KEYPAD_FOUR, 
            -Keycode.ALT]),
        (0x202000, 'Tongue', [':p', Keycode.SPACE]),
        (0x202000, 'wink', [';)', Keycode.SPACE]),
        # 4th row ----------
        (0x202000, 'straight', [':|', Keycode.SPACE]),
        (0x202000, 'sad', [':(', Keycode.SPACE]),
        (0x202000, 'happy', [':)', Keycode.SPACE]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}