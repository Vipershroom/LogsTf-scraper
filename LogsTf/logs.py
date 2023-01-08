from bs4 import BeautifulSoup
import requests
from math import ceil
from constants import url

class LogsTf:
    
    # Takes in player_id and formats it into a link.
    def __init__(self, player_id):
        self.player_id = player_id
        
    # Gets latest log from the user
    def get_latest_log(self) -> str:
        source = requests.get(f"{url}/{self.player_id}").text
        return f"{url}/{BeautifulSoup(source, 'lxml').find('td').a['href']}"
    
    """Takes in the amount of logs the user wants. Then
    calculates how many pages would be needed to get that many logs and
    returns them in a list."""
    def __get_page_range(self, page_range: int) -> list:
        num = ceil(page_range / 25)
        return [f"{url}/profile/{self.player_id}?p={i}" for i in range(1,num+1)]
    

    
n = LogsTf("76561198322448472")
print(n.get_page_range(75))