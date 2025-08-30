from dotenv import load_dotenv
import os
import numpy
import skillaroo
import player as p
from colorama import Fore

class Team:
    team_name: str = ""
    players: list[p.Player] = []
    avg_rating: int = 0
    team_ratin: int = 0
    wins: int = 0
    matches: int = 0
    
    def __init__(self, *, team_name: str = "noname", players: list[p.Player] = [], min_team_size: int = 1, max_team_size: int = 5) -> None:
        total_rating: int = 0
        players_queue: list[p.Player] = []
        avg_rating: int = 0
        
        # if (not team_name)
        
        # # Checks for team size, else compares to default values
        # if (len(players) < int(os.getenv("MIN_TEAM_SIZE") or 1)):
        #     print (f"{Fore.RED}Team not created: Team size lower than minimum")
        #     pass
        
        # # Checks for team size, else compares to default values
        # if (len(players) > int(os.getenv("MAX_TEAM_SIZE") or 5)):
        #     print (f"{Fore.RED}Team not created: Team size larger than maximum")
        #     pass
        
        # Checks for length
        

        for player in players:
            players_queue.append(player)
            
        for player in players_queue:
            total_rating = total_rating + player.rating
            
        avg_rating = total_rating / len(players_queue)
        
        self.avg_rating = avg_rating
        self.team_name = team_name
        
            