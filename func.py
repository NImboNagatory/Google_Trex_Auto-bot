from pyautogui import click, pixel, locateOnScreen, press, keyUp, keyDown
from webbrowser import open
from time import sleep, time


class Trex_Wrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        self.jump_dist = 140
        open("https://elgoog.im/t-rex/v2/", new=1)

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 29)
            press('up')

    def check_obstacle(self):
        while True:
            if self.pixel_catcher():
                press('up')
                sleep(0.2)
                press('down')

    def pixel_catcher(self):
        pixel_i_ = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 30)[0]
        if pixel_i_ < 247:
            return True
        else:
            return False
