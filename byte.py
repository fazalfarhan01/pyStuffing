from pyStuffing import ByteStuffing
from pyStuffing import clear


if __name__ == "__main__":
    stuff = ByteStuffing(list("abcdefghijklmnopqrstuvwxyz".upper()), escape_character="E", flag_character="F")
    # stuff = ByteStuffing()
    stuff.startStuffing()
    stuff.startUnStuffing()

    clear()

    print("Sequence:  {}".format(stuff.sequence))
    print("Stuffed:   {}".format(stuff.stuffed))
    print("Un-stuffed: {}".format(stuff.unStuffed))