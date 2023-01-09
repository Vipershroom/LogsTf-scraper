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
    
    """Returns the amount of logs the user wants
    in the form of a list. Logs are returned as links."""
    def get_logs(self, amount: int) -> list:
        
        # Gets the amount of pages to loop over.
        page_links = self.__get_page_range(amount)
        
        log_list = []
        
        # Makes sure the log count doesn't go over the specified amount
        counter = 0
        
        for links in page_links:
            for logs in BeautifulSoup(requests.get(links).text, 'lxml').find_all('td'):
                if logs.a != None and counter < amount:
                    log_list.append(f"{url}/{logs.a['href']}")
                    counter += 1
        return log_list            

    # Gets the data of a single log and returns a dictionary
    def get_data(self, log_link: str) -> dict:
        
        content = BeautifulSoup(requests.get(log_link).text, 'lxml').find('tr', id=f'player_{self.player_id}')
        
        # Stores all the data into a dictionary and returns it
        return self.__store_data([content.find_all('td', class_=None)[i].text for i in range(13)])
    
    # Stores log data into a dictionary
    def __store_data(self, log: list) -> dict:
        return {
            "Kills": log[0],
            "Assists": log[1],
            "Deaths": log[2],
            "Damage": log[3],
            "Damage / Minute": log[4],
            "Kills and Assists / Deaths": log[5],
            "Kills / Deaths": log[6],
            "Damage Taken": log[7],
            "Damage Taken / Minute": log[8],
            "Health pickups": log[9],
            "Backstabs": log[10],
            "Headshots": log[11],
            "Capture Points Captures": log[12],
        }
            
            
    
    
n = LogsTf("76561198322448472")
print(n.get_data(n.get_logs(26)[0]))