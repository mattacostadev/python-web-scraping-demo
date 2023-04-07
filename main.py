from web import WebSurfer
from bs4 import BeautifulSoup

import string

base_pfr_url = 'https://www.pro-football-reference.com/players/'

surfer = WebSurfer()

# Get all PFR active player IDs by first letter of last name
def scrape_active_player_ids():
    alphabet = string.ascii_uppercase
    id_list = []

    for letter in alphabet:
        print(f'Fetching {letter} player IDs...')

        # Get page for letter
        html = surfer.get_page(base_pfr_url + letter)

        # Get element containing player list from page HTML, get active player elements from list
        players = BeautifulSoup(html, features='html.parser').find(id='div_players').find_all(name='b')

        for player in players:
            print(player)

            player_id_str = str(player.a.attrs['href'])
            print(f'-> {player_id_str}')
            player_id_str = player_id_str[:-4][11:]
            print(f'-> {player_id_str}')

            id_list.append(player_id_str)

    return id_list

if __name__ == "__main__":
    active_player_ids = scrape_active_player_ids()