import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
keyboard=KMKKeyboard()
keyboard.rows_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D3, board.D4, board.D5)
keyboard.Diode_Orientation = Diode_Orientation.COL2ROW
keyboard.Keymap = [
    [KC.q, KC.w, KC.e]
    [KC.a, KC.r, KC.f]
    [KC.z, KC.x, KC.V]
]
if __name__ == "__main__":
    keyboard.go()
    