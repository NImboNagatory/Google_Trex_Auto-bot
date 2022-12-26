from func import Trex_Wrecker

cheat = Trex_Wrecker()
while cheat.trex_location is None:
    cheat.find_trex()
cheat.check_obstacle()
