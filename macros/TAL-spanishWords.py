# MACROPAD Hotkeys example: TAL Palabras en español

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Palabras en espa~nol', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x252500, 'much tnx', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            Keycode.KEYPAD_SIX, -Keycode.KEYPAD_SIX,
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            -Keycode.ALT,'Muchas Gracias!']),
        (0x002525, "morn", ['Buenos d',Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, 
            Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE,
            Keycode.KEYPAD_SEVEN, -Keycode.KEYPAD_SEVEN, 
            -Keycode.ALT,'as']),
        (0x250025, "even'n", ['Buenas noches']),
        # 2nd row ----------
        (0x252500, 'tnx', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            Keycode.KEYPAD_SIX, -Keycode.KEYPAD_SIX,
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            -Keycode.ALT,'Gracias!']),
        (0x002525, "a'noon", ['Buenas tardes']),
        (0x250025, 'nachos', [Keycode.ALT, 
            Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, 
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            Keycode.KEYPAD_SIX, -Keycode.KEYPAD_SIX,
            Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, 
            -Keycode.ALT,'Buenos Nachos!']),
        # 3rd row ----------
        (0x200010, 'ohms', [Keycode.ALT, 
            Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, 
            Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE,
            Keycode.KEYPAD_FOUR, -Keycode.KEYPAD_FOUR, 
            -Keycode.ALT]),
        (0x200030, 'Tongue', [':p', Keycode.SPACE]),
        (0x200050, 'wink', [';)', Keycode.SPACE]),
        # 4th row ----------
        (0x201000, 'straight', [':|', Keycode.SPACE]),
        (0x205000, 'sad', [':(', Keycode.SPACE]),
        (0x209000, 'happy', [':)', Keycode.SPACE]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}