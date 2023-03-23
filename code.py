# Home Office mouse which moves in a rectangle shape
# Credit: https://github.com/smnkrisz/HO-mouse

import board
import digitalio
import time
import usb_hid
from adafruit_hid.mouse import Mouse

# Components as variables
mouse = Mouse(usb_hid.devices)
led_onboard = digitalio.DigitalInOut(board.LED)
led_onboard.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Default values
led_onboard.value = False
mouse_move = 150
mouse_pause = 120

while True:
    if button.value:
        for number in range(5):
            
            mouse.move(x=-mouse_move)            
            time.sleep(mouse_pause)

            mouse.move(y=-mouse_move)
            time.sleep(mouse_pause)

            mouse.move(x=mouse_move)
            time.sleep(mouse_pause)

            mouse.move(y=mouse_move)
            time.sleep(mouse_pause)
