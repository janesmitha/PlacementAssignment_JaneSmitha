'''Question 3: -'''
'''Write a program, which would download the data from the provided link, and then read the data and convert
that into properly structured data and return it in Excel format.
Note - Write comments wherever necessary explaining the code written.

Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
Data Attributes - id: Identification Number - int num: Number of the
● Pokémon in the official Pokédex - int name: Pokémon name -
● string img: URL to an image of this Pokémon - string type:
● Pokémon type -string height: Pokémon height - float
● weight: Pokémon weight - float candy: type of candy used to evolve Pokémon or
given
● when transferred - string candy_count: the amount of candies required to evolve
- int
● egg: Number of kilometers to travel to hatch the egg - float spawn_chance:
● Percentage of spawn chance (NEW) - float avg_spawns: Number of this
pokemon on 10.000 spawns (NEW) - int
● spawn_time: Spawns most active at the time on this field. Spawn times are the same for all
time zones and are expressed in local time. (NEW) - “minutes: seconds” multipliers:
Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int
weakness: Types of
● Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of
successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous
evolutions of Pokémon - - list of dict '''

import requests
import json
import pandas as pd

# Step 1: Import necessary libraries

# Step 2: Download the data
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Step 3: Read and parse the data

# Step 4: Extract the required information
structured_data = []
for pokemon in data["pokemon"]:
    attributes = {
        "id": pokemon["id"],
        "num": pokemon["num"],
        "name": pokemon["name"],
        "img": pokemon["img"],
        "type": pokemon["type"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "candy": pokemon.get("candy", ""),
        "candy_count": pokemon.get("candy_count", 0),
        "egg": pokemon.get("egg", ""),
        "spawn_chance": pokemon.get("spawn_chance", 0.0),
        "avg_spawns": pokemon.get("avg_spawns", 0),
        "spawn_time": pokemon.get("spawn_time", ""),
        "multipliers": pokemon.get("multipliers", []),
        "weakness": pokemon.get("weaknesses", []),
        "next_evolution": pokemon.get("next_evolution", []),
        "prev_evolution": pokemon.get("prev_evolution", [])
    }
    structured_data.append(attributes)

# Step 5: Convert the data into a pandas DataFrame
df = pd.DataFrame(structured_data)

# Step 6: Save the data in Excel format
df.to_excel("pokemon_data.xlsx", index=False)
