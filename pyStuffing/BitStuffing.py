from typing import Counter
from colorama import Fore
# from .cls import cls


class BitStuffing(object):
    def __init__(self, sequence: list = None):
        if sequence == None:
            sequence = input("Enter the sequence (No Spaces): ")
            sequence = list(map(int, list(sequence)))
        self.sequence = sequence
        self.bitFlag = "{}0, 1, 1, 1, 1, 1, 1, 0{}".format(
            Fore.LIGHTRED_EX, Fore.RESET)
        self.count = 0
        self.stuffed = []
        self.stuffedColored = ""
        self.unStuffed = []

    def startStuffing(self):
        self.stuffed = list(
            map(int, list("".join(list(map(str, self.sequence))).replace("11111", "111110"))))

    def getStuffedColored(self) -> str:
        return "[{}]".format(", ".join(list(map(str, self.stuffed))).replace("1, 1, 1, 1, 1, 0", "1, 1, 1, 1, 1, {}0{}".format(Fore.LIGHTRED_EX, Fore.RESET)))

    def startUnstuffing(self):
        self.unStuffed = list(
            map(int, list("".join(list(map(str, self.sequence))).replace("111110", "11111"))))


if __name__ == "__main__":
    stuff = BitStuffing([0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
    stuff.startStuffing()
    stuff.startUnstuffing()
    # cls()
    print("Main Sequence:       {}".format(stuff.sequence))
    print("Stuffed Sequence:    {}".format(stuff.stuffed))
    print("Un-Stuffed Sequence: {}".format(stuff.unStuffed))
    print("Stuffed Sequence:    {}".format(stuff.getStuffedColored()))
