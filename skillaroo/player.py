# import numpy as np
from dotenv import load_dotenv
from colorama import Fore
import os

load_dotenv()
class Player:
    name = ""
    rating = 0
    matches = 0
    wins = 0
    winrate = 0
    
    # Class constructor
    # Required args: name
    def __init__(self, name : str, rating = None) -> None:
        
        self.name = name
        # If rating is not provided, defaults to 1000
        self.rating = rating or int(os.getenv("DEFAULT_RATING") or 1000)
        
    def __str__(self) -> str:
        return (f"{Fore.WHITE}{self.name} | Rating : {self.rating} | Matches : {self.matches} | Wins : {self.wins} | Winrate : {self.winrate * 100} %")
    
    def set_rating(self, rating : int) -> int:
        if rating < int(os.getenv("LOWEST_RATING") or 0):
            print(f"{Fore.RED}Unable to set rating: Rating below minimum threshold")
            return -22
        
        self.rating = rating
        print(f"{Fore.GREEN}Rating set! {self.name} at {self.rating}")
        return 0
    
    def adjust_rating (self, rating : int) -> int:
        if (int(self.rating) - rating) < int(os.getenv("LOWEST_RATING") or 0):
            print(f"{Fore.RED}Unable to set rating: Rating below minimum threshold")
            return -22
        return 0
    
    def add_win (self) -> int:
        self.wins = self.wins + 1
        return 0
    
    def remove_win (self) -> int:
        self.wins = self.wins - 1
        return 0