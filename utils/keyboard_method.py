from time import sleep

from pykeyboard import PyKeyboard
from pymouse import PyMouse

k = PyKeyboard()


class Keyboard_method:

    def keyboard_enter(self):
        k.tap_key(k.enter_key) # 保存


    def close_wps(self):
        k.press_key(k.alt_key)
        k.tap_key(k.function_keys[4])
        k.release_key(k.alt_key)