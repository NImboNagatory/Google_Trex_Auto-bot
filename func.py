from pyautogui import typewrite, click, pixelMatchesColor, pixel, locateOnScreen, locateCenterOnScreen, keyDown, keyUp, press
from webbrowser import open
from time import sleep


class Trex_wrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        open("https://elgoog.im/t-rex/v2/", new=1)

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + 160, self.trex_location[1] + 38)
            press('up')

    def check_obst(self):
        pixel_cactus = pixel(self.trex_location[0] + 160, self.trex_location[1] + 38)[0]
        pixel_bird = pixel(self.trex_location[0]+120, self.trex_location[1]-2)[0]
        if pixel_cactus < 247:
            press('up')
        elif pixel_bird < 247:
            keyDown("down")
            sleep(1)
            keyUp("down")


