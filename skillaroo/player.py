# import numpy as np
from dotenv import load_dotenv
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
        self.rating = rating or os.getenv("DEFAULT_RATING")
        
    def __str__(self) -> str:
        return (f"{self.name} | Rating : {self.rating} | Matches : {self.matches} | Wins : {self.wins} | Winrate : {self.winrate * 100} %")