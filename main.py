from func import Trex_wrecker

cheat = Trex_wrecker()
while cheat.trex_location is None:
    cheat.find_trex()


def infinity():
    while True:
        yield


for _ in infinity():
    cheat.check_obstacle()
