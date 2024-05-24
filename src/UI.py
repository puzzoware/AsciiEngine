import Engine
import os
import sys

class UI():
    """
    This class houses the user interface for the game
    interface(self): Houses the function for the user interfaces
    """
    def __init__(self) -> None:
        default = "/text/1.txt"
    
    def interface(self):
        print("welcome to the ASCII game generator")
        print ("choose an option:\n 1: create new game\n 2: exit")
        choice = input("Choice:")
        if choice == 1:
            self.gameGen()
        if choice ==2:
            exit()
        else:
            print("please pick one or two")
            self.interface()

    def gameGen(self):
        game = Engine.Engine()
        print("enter the location of the first text files OR leave blank for\n default (/text/1.txt)")


    