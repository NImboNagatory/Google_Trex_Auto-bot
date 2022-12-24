from pyautogui import click, pixel, locateOnScreen, press
from webbrowser import open
from time import time


class Trex_wrecker:
    def __init__(self):
        self.Day_Night = "Day"
        self.trex_location = None
        self.jump_dist = 160
        open("https://elgoog.im/t-rex/v2/", new=1)

    def find_trex(self):
        trex_location = locateOnScreen('data/Trex.PNG')
        if trex_location is not None:
            self.trex_location = trex_location
            click(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 22)
            press('up')

    def check_obstacle(self):
        # pixel_cactus = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 22)[0]
        # pixel_cactus_smol = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 31)[0]
        # pixel_bird = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1])[0]

        for Pixel in range(9):
            pixel_a = pixel(self.trex_location[0] + self.jump_dist-3, self.trex_location[1] + 22 + Pixel)[0]
            pixel_b = pixel(self.trex_location[0] + self.jump_dist-2, self.trex_location[1] + 22 + Pixel)[0]
            pixel_c = pixel(self.trex_location[0] + self.jump_dist-1, self.trex_location[1] + 22 + Pixel)[0]
            pixel_d = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1] + 22 + Pixel)[0]
            pixel_e = pixel(self.trex_location[0] + self.jump_dist + 1, self.trex_location[1] + 22 + Pixel)[0]
            pixel_f = pixel(self.trex_location[0] + self.jump_dist + 2, self.trex_location[1] + 22 + Pixel)[0]
            pixel_i = pixel(self.trex_location[0] + self.jump_dist + 3, self.trex_location[1] + 22 + Pixel)[0]
            pixel_bird = pixel(self.trex_location[0] + self.jump_dist, self.trex_location[1])[0]
            if pixel_a < 247 or pixel_b < 247 or pixel_c < 247 or pixel_d < 247 or pixel_e < 247 or pixel_f < 247 or pixel_i < 247:
                press('up')
                self.jump_dist += 2
            elif pixel_bird < 247:
                start = time()
                while time() - start < 100:
                    press('down')
                    self.jump_dist += 2

        # if pixel_cactus < 247:
        #     self.jump_dist += 2
        #     press('up')
        # if pixel_cactus_smol < 247:
        #     self.jump_dist += 2
        #     press('up')
        # if pixel_bird < 247:
        #     start = time()
        #     while time() - start < 100:
        #         self.jump_dist += 2
        #         press('down')
