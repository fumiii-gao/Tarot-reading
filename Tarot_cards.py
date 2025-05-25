import os
import random

class Tarotcard:
    def __init__(self,number,name,meaning,suit,yes_or_no,inversed_meaning,ascii_art,suit_number):
        self.number = number
        self.name = name
        self.meaning = meaning
        self.suit = suit
        self.yes_or_no = yes_or_no
        self.inversed_meaning = inversed_meaning
        self.ascii_art = ascii_art
        self.suit_number = suit_number
   #define tarot card

    def display_Daily(self,ascii_folder='ascii_cards'):
        print(f'Name: {self.name} [Upright]')
        print(f'Meaning: {self.meaning}')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ascii_folder = os.path.join(script_dir,  'ascii_cards')
        ascii_path = os.path.join(ascii_folder, self.ascii_art)
        if os.path.exists(ascii_path):
            with open(ascii_path, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"(ASCII art not found at: {ascii_path})")

    def display_YoN(self,ascii_folder='ascii_cards'):
        print(f'Name:{self.name}')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ascii_folder = os.path.join(script_dir,  'ascii_cards')
        ascii_path = os.path.join(ascii_folder, self.ascii_art)
        if os.path.exists(ascii_path):
            with open(ascii_path, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"(ASCII art not found at: {ascii_path})")
        print(self.yes_or_no)

    def display_cus(self,ascii_folder='ascii_cards'):
        try:
            print(f'Name:{self.name} [{self.orientation}]')
        except AttributeError:
            print(f'Name: {self.name} [Upright]')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ascii_folder = os.path.join(script_dir,  'ascii_cards')
        ascii_path = os.path.join(ascii_folder, self.ascii_art)
        if os.path.exists(ascii_path):
            with open(ascii_path, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"(ASCII art not found at: {ascii_path})")
        

    def display_show(self,ascii_folder='ascii_cards'):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ascii_folder = os.path.join(script_dir,  'ascii_cards')
        ascii_path = os.path.join(ascii_folder, self.ascii_art)
        if os.path.exists(ascii_path):
            with open(ascii_path, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"(ASCII art not found at: {ascii_path})")
        print(f'Name: {self.name}')
        print(f'Meaning: {self.meaning}')
        print(f'Suit: {self.suit}')
        print(f'Yes or no: {self.yes_or_no}')
        print(f'Inversed meaning: {self.inversed_meaning}')
   
#define how cards show in 3 different functions
#ascii art from github@Kathryn Isabelle Lawrence