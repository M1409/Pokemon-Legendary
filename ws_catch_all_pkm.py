import requests
from bs4 import BeautifulSoup
import csv

url = "https://pokemondb.net/pokedex/all"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'pokedex'})

    with open('pokemon_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Pokedex ID','Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
        
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 10:
                pokedex_id = columns[0].text.strip()
                name = columns[1].text.strip()
                pokemon_type = columns[2].text.strip()
                total = columns[3].text.strip()
                hp = columns[4].text.strip()
                attack = columns[5].text.strip()
                defense = columns[6].text.strip()
                sp_atk = columns[7].text.strip()
                sp_def = columns[8].text.strip()
                speed = columns[9].text.strip()

                csv_writer.writerow([pokedex_id,name, pokemon_type, total, hp, attack, defense, sp_atk, sp_def, speed])
    print("Dados salvos com sucesso em 'pokemon_data.csv'.")
