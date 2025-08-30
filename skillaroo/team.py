from dotenv import load_dotenv
import os
import numpy
import skillaroo
import player as p
from colorama import Fore

class Team:
    team_name = ""
    players = []
    avg_rating = 0
    team_rating = 0
    wins = 0
    matches = 0
    
    def __init__(self, team_name: str, *players: p.Player) -> None:
        total_rating = 0
        players_queue = []
        avg_rating = 0
        
        # Checks for team size, else compares to default values
        if (len(players) < int(os.getenv("MIN_TEAM_SIZE") or 1)):
            print (f"{Fore.RED}Team not created: Team size lower than minimum")
            pass
        
        # Checks for team size, else compares to default values
        if (len(players) > int(os.getenv("MAX_TEAM_SIZE") or 5)):
            print (f"{Fore.RED}Team not created: Team size larger than maximum")
            pass
        
        # Checks for length
        
        
        for player in players:
            players_queue.append(player)
            
        for player in players_queue:
            total_rating = total_rating + player.rating
            
        avg_rating = total_rating / len(players_queue)
        self.avg_rating = avg_rating
        self.team_name = team_name
        
            