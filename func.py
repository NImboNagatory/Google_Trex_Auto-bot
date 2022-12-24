from pyautogui import typewrite, click, pixelMatchesColor, pixel, locateOnScreen, locateCenterOnScreen, keyDown, keyUp, press
from webbrowser import open
from time import sleep


class Trex_wrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        self.open_website()

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + 140, self.trex_location[1] + 29)
            self.jump()

    def check_obst(self):
        pixel_cactus = pixel(self.trex_location[0] + 155, self.trex_location[1] + 29)
        pixel_bird = pixel(self.trex_location[0]+120, self.trex_location[1]-2)
        if pixel_cactus[0] < 247 or pixel_cactus[1] < 247 or pixel_cactus[2] < 247:
            self.jump()
        elif pixel_bird[0] < 247 or pixel_bird[1] < 247 or pixel_bird[2] < 247:
            self.duck()

    def open_website(self):
        open("https://elgoog.im/t-rex/v2/", new=1)

    def jump(self):
        press('up')

    def duck(self):
        keyDown("down")
        sleep(1)
        keyUp("down")
