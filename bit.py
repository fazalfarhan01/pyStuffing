from pyStuffing import BitStuffing
from pyStuffing import clear

if __name__ == "__main__":
    stuff = BitStuffing()
    stuff.startStuffing() # START STUFFING
    stuff.startUnstuffing()

    clear() # CLEAR SCREEN

    # PRINT SEQUENCES TO SCREEN
    print("Main Sequence:       {}".format(stuff.sequence))
    print("Stuffed Sequence:    {}".format(stuff.stuffed))
    print("Un-Stuffed Sequence: {}".format(stuff.unStuffed))
    print("Stuffed Sequence:    {}".format(stuff.getStuffedColored()))