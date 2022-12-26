from pyautogui import click, pixel, locateOnScreen, press, keyUp, keyDown, screenshot
from webbrowser import open
from time import sleep


class TrexWrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        self.jump_dist = 137
        open("https://elgoog.im/t-rex/v2/", new=1)

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        # finds trex location on screen and saves its coordinates
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + self.jump_dist, self.trex_location[1])
            press('up')

    def check_obstacle(self):
        # infinite loop
        for _ in iter(int, 1):
            src = screenshot()
            pix_c = src.getpixel((self.trex_location[0] + self.jump_dist, self.trex_location[1] + 28))[0]
            # check if cactus is ahead
            if pix_c < 247:
                press('up')
                sleep(0.18)
                keyDown('down')
                sleep(0.06)
                keyUp('down')
            else:
                # check if bird is up ahead
                pix_b = src.getpixel((self.trex_location[0] + self.jump_dist, self.trex_location[1] - 2))[0]
                if pix_b < 247:
                    keyDown('down')
                    sleep(0.5)
                    keyUp('down')
