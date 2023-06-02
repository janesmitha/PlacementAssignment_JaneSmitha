'''Using the data from Question 3, write code to analyze the data and answer the following questions Note 1.
Draw plots to demonstrate the analysis for the following questions for better visualizations.
2. Write code comments wherever required for code understanding
Insights to be drawn -
● Get all Pokemons whose spawn rate is less than 5%
● Get all Pokemons that have less than 4 weaknesses
● Get all Pokemons that have no multipliers at all
● Get all Pokemons that do not have more than 2 evolutions
● Get all Pokemons whose spawn time is less than 300 seconds.
Note - spawn time format is "05:32”, so assume “minute: second” format and perform the analysis.
● Get all Pokemon who have more than two types of capabilities'''
import requests
import matplotlib.pyplot as plt

# Step 1: Read and load the JSON data
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Step 2: Extract the required information
pokemons = data["pokemon"]

# Lists to store the results for each question
spawn_rate_less_than_5 = []
less_than_4_weaknesses = []
no_multipliers = []
less_than_2_evolutions = []
spawn_time_less_than_300 = []
more_than_2_capabilities = []

# Step 3: Analysis and answering the questions
for pokemon in pokemons:
    # Question 1: Get all Pokemons whose spawn rate is less than 5%
    spawn_rate = float(pokemon["spawn_chance"])
    if spawn_rate < 5:
        spawn_rate_less_than_5.append(pokemon)

    # Question 2: Get all Pokemons that have less than 4 weaknesses
    weaknesses_count = len(pokemon["weaknesses"])
    if weaknesses_count < 4:
        less_than_4_weaknesses.append(pokemon)

    # Question 3: Get all Pokemons that have no multipliers at all
    multipliers = pokemon.get("multipliers")
    if not multipliers:
        no_multipliers.append(pokemon)

    # Question 4: Get all Pokemons that do not have more than 2 evolutions
    evolutions_count = len(pokemon.get("next_evolution", []))
    if evolutions_count <= 2:
        less_than_2_evolutions.append(pokemon)

    # Question 5: Get all Pokemons whose spawn time is less than 300 seconds
    spawn_time = pokemon["spawn_time"]
    if spawn_time != "N/A":
        minutes, seconds = map(int, spawn_time.split(":"))
        total_seconds = minutes * 60 + seconds
        if total_seconds < 300:
            spawn_time_less_than_300.append(pokemon)

    # Question 6: Get all Pokemon who have more than two types of capabilities
    capabilities_count = len(pokemon["type"])
    if capabilities_count > 2:
        more_than_2_capabilities.append(pokemon)

# Step 4: Visualization
# Plotting the number of Pokemons for each question
labels = ["Spawn Rate < 5%", "Weaknesses < 4", "No Multipliers", "Evolutions <= 2", "Spawn Time < 300s", "Capabilities > 2"]
values = [
    len(spawn_rate_less_than_5),
    len(less_than_4_weaknesses),
    len(no_multipliers),
    len(less_than_2_evolutions),
    len(spawn_time_less_than_300),
    len(more_than_2_capabilities)
]

plt.bar(labels, values)
plt.xlabel("Questions")
plt.ylabel("Number of Pokemons")
plt.title("Analysis of Pokémon Data")
plt.xticks(rotation=45)
plt.show()

# Printing the results
print("Pokemons whose spawn rate is less than 5%:")
for pokemon in spawn_rate_less_than_5:
    print(pokemon["name"])

print("\nPokemons that have less than 4 weaknesses:")
for pokemon in less_than_4_weaknesses:
    print(pokemon["name"])

print("\nPokemons that have no multipliers at all:")
for pokemon in no_multipliers:
    print(pokemon["name"])

print("\nPokemons that do not have more than 2 evolutions:")
for pokemon in less_than_2_evolutions:
    print(pokemon["name"])

print("\nPokemons whose spawn time is less than 300 seconds:")
for pokemon in spawn_time_less_than_300:
    print(pokemon["name"])

print("\nPokemon who have more than two types of capabilities:")
for pokemon in more_than_2_capabilities:
    print(pokemon["name"])
