from pyStuffing.ByteStuffing import ByteStuffing
from pyStuffing.cls import cls


if __name__ == "__main__":
    # stuff = ByteStuffing(list("abcdefghijklmnopqrstuvwxyz".upper()))
    stuff = ByteStuffing()
    stuff.startStuffing()
    stuff.startUnStuffing()

    cls()
    
    print("Sequence:  {}".format(stuff.sequence))
    print("Stuffed:   {}".format(stuff.stuffed))
    print("Un-stuffed: {}".format(stuff.unStuffed))