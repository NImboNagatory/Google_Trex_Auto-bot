from func import TrexWrecker

cheat = TrexWrecker()
while cheat.trex_location is None:
    cheat.find_trex()
cheat.check_obstacle()
