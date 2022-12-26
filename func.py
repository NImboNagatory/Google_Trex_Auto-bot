from pyautogui import click, pixel, locateOnScreen, press, keyUp, keyDown
from webbrowser import open
from time import sleep


class TrexWrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        self.jump_dist = 140
        open("https://elgoog.im/t-rex/v2/", new=1)

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + self.jump_dist, self.trex_location[1])
            press('up')

    def check_obstacle(self):
        while True:
            pix_data = self.pixel_catcher()
            if pix_data == "Cactus":
                press('up')
                sleep(0.2)
                keyDown('down')
                keyUp('down')
            elif pix_data == "Pterosaurs":
                keyDown('down')
                sleep(0.5)
                keyUp('down')

    def pixel_catcher(self):
        pixel_c_ = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 29)[0]
        if pixel_c_ < 247:
            return "Cactus"

        pixel_b_ = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1]-2)[0]
        if pixel_b_ < 247:
            return "Pterosaurs"
