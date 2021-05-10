from typing import Counter
from colorama import Fore
# from .cls import cls

class BitStuffing(object):
    def __init__(self, sequence:list=None):
        if sequence == None:
            sequence = input("Enter the sequence (No Spaces): ")
            sequence = list(map(int, list(sequence)))
        self.sequence = sequence
        self.bitFlag = "{}0, 1, 1, 1, 1, 1, 1, 0{}".format(Fore.LIGHTRED_EX, Fore.RESET)
        self.count = 0
        self.stuffed = []
        self.stuffedColored = ""
        self.unStuffed = []

        # self.startStuffing()
        # self.startUnstuffing()
    
    def startStuffing(self):
        for bit in self.sequence:
            if self.count == 5:
                self.stuffed.append(0)
                self.addColoredBit(0,True)
                self.count = 0

            self.stuffed.append(bit)
            self.addColoredBit(bit)

            if bit == 1:
                self.count += 1
            else:
                self.count = 0

    def addColoredBit(self,bit:int, added:bool=False):
        if len(self.stuffedColored) == 0:
            self.stuffedColored = "["
        else:
            self.stuffedColored =  self.stuffedColored.replace("]",",")
        if added:
            self.stuffedColored += "{}{}{} ]".format(Fore.LIGHTGREEN_EX, bit, Fore.RESET)
        else:
            self.stuffedColored += "{} ]".format(bit)
    
    def getStuffedColored(self) -> str:
        return "[{}, {}, {}]".format(self.bitFlag, self.stuffedColored[1:-1], self.bitFlag)

    def startUnstuffing(self):
        self.count = 0
        for bit in self.stuffed:
            if self.count == 5:
                self.count = 0
                continue
            if bit == 1:
                self.count += 1
            self.unStuffed.append(bit)
        


if __name__ == "__main__":
    stuff = BitStuffing([0,0,1,0,1,1,1,1,1,1,1,1,1,1,0])
    stuff.startStuffing()
    stuff.startUnstuffing()
    # cls()
    print("Main Sequence:       {}".format(stuff.sequence))
    print("Stuffed Sequence:    {}".format(stuff.stuffed))
    print("Un-Stuffed Sequence: {}".format(stuff.unStuffed))
    print("Stuffed Sequence:    {}".format(stuff.getStuffedColored()))