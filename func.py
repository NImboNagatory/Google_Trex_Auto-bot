from pyautogui import click, pixel, locateOnScreen, press
from webbrowser import open
from time import time


class Trex_Wrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        self.jump_dist = 180
        open("https://elgoog.im/t-rex/v2/", new=1)

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 22)
            press('up')

    def check_obstacle(self):

        for Pixel in range(9):
            pixel_a_ = pixel(self.trex_location[0] + self.jump_dist-8, self.trex_location[1] + 22 + Pixel)[0]
            pixel_b_ = pixel(self.trex_location[0] + self.jump_dist-4, self.trex_location[1] + 22 + Pixel)[0]
            pixel_c_ = pixel(self.trex_location[0] + self.jump_dist-2, self.trex_location[1] + 22 + Pixel)[0]
            pixel_d_ = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 31)[0]
            pixel_e_ = pixel(self.trex_location[0] + self.jump_dist + 2, self.trex_location[1] + 31 - Pixel)[0]
            pixel_f_ = pixel(self.trex_location[0] + self.jump_dist + 4, self.trex_location[1] + 31 - Pixel)[0]
            pixel_i_ = pixel(self.trex_location[0] + self.jump_dist + 8, self.trex_location[1] + 31 - Pixel)[0]
            if pixel_i_ < 247 or pixel_f_ < 247 or pixel_e_ < 247 or pixel_d_ < 247 or pixel_c_ < 247 or pixel_b_ < 247 or pixel_a_ < 247:
                self.jump_dist += 2
                press('up')
            # elif pixel_bird_a < 247 or pixel_bird < 247 or pixel_bird_b < 247:
            #     start = time()
            #     self.jump_dist += 2
            #     while time() - start < 100:
            #         press('down')

