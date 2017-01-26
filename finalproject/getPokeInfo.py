# Call the PokéAPI to make a list of Pokémon sprite URLs, type advantages, and attacks
import csv
import requests
import pandas as pd

# Sprites for every Pokemon
"""imgFile = open("pokeSprites.csv", 'w')
imgFileWriter = csv.writer(imgFile, delimiter = ',')
imgFileWriter.writerow(["#", "URL"])
for x in range(1, 722):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(x) + "/"
    print(url)
    
    info = requests.get(url).json()
    imgFileWriter.writerow([str(x), info['sprites']['front_default']])
"""

# Every move and its type
"""moveFile = open("pokeAttacks.csv", 'w')
moveFileWriter = csv.writer(moveFile, delimiter = ',')
moveFileWriter.writerow(["#", "Name", "Type"])
for x in range(1, 622):
    url = "https://pokeapi.co/api/v2/move/" + str(x) + "/"
    print(url)
    
    info = requests.get(url).json()
    moveFileWriter.writerow([str(x), info['name'], info['type']['name']])
"""

# Types and their matchups
"""typeFile = open("pokeTypes.csv", 'w')
typeFileWriter = csv.writer(typeFile, delimiter = ',')
typeFileWriter.writerow(["#", "Name", "Half Dmg From", "No Dmg From", "Half Dmg To", "Double Dmg From", "No Damage To", "Double Dmg To"])
for x in range(1, 19):
    url = "https://pokeapi.co/api/v2/type/" + str(x) + "/"
    print(url)
    
    info = requests.get(url).json()
    typeFileWriter.writerow([str(x), info['name'], [info['damage_relations']['half_damage_from'][x]['name'] for x in range(len(info['damage_relations']['half_damage_from']))], [info['damage_relations']['no_damage_from'][x]['name'] for x in range(len(info['damage_relations']['no_damage_from']))], [info['damage_relations']['half_damage_to'][x]['name'] for x in range(len(info['damage_relations']['half_damage_to']))], [info['damage_relations']['double_damage_from'][x]['name'] for x in range(len(info['damage_relations']['double_damage_from']))], [info['damage_relations']['no_damage_to'][x]['name'] for x in range(len(info['damage_relations']['no_damage_to']))], [info['damage_relations']['double_damage_to'][x]['name'] for x in range(len(info['damage_relations']['double_damage_to']))]])
"""

# Moves that each Pokemon has
"""movesetFile = open("pokeMoveset.csv", 'w')
movesetFileWriter = csv.writer(movesetFile, delimiter = ',')
movesetFileWriter.writerow(['#', "Name", "Moves"])
for x in range(1, 722):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(x) + "/"
    print(url)
    
    info = requests.get(url).json()
    movesetFileWriter.writerow([str(x), info['name'], [info['moves'][x]['move']['name'] for x in range(len(info['moves']))]])
"""

# Count number of moves of each type that each Pokemon has
"""pokemonList = pd.read_csv("Pokemon.csv")
movesetList = pd.read_csv("pokeMoveset.csv")
attackList = pd.read_csv("pokeAttacks.csv")
moveTypeFile = open("pokeMoveTypes.csv", 'w')
moveTypeFileWriter = csv.writer(moveTypeFile, delimiter = ',')
moveTypeFileWriter.writerow(["#", "Name", "Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"])
for x in pokemonList['Name']:
    
"""