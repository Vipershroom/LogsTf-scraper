from bs4 import BeautifulSoup
import requests
from math import ceil
from constants import url

class LogsTf:
    
    # Takes in player_id and formats it into a link.
    def __init__(self, player_id):
        self.player_id = f"{url}/profile/{player_id}"
        
    # Gets latest log from the user
    def get_latest_log(self):
        source = requests.get(self.player_id).text
        return f"{url}/{BeautifulSoup(source, 'lxml').find('td').a['href']}"
    
n = LogsTf("76561198322448472")
print(n.get_latest_log())