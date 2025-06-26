from pokemon import Pokemon

# Method to check and return pokemon names that match input type
def get_by_type(pokemons: list[Pokemon], type: str):
    res = []
    for pok in pokemons:
        if type in pok.types:
            res.append(pok.name)
    return res

# Method to track and return list of names of pokemons it can evolve into
def get_evolutionary_line(pok:Pokemon):
    res = []
    while pok:
        res.append(pok.name)
        pok = pok.evolution

    return res
# Test get_by_type method
# pok1 = Pokemon("Pikachu", ['Electric', 'dynamic', 'normal'])
# pok2 = Pokemon("Mucho", ['dynamic'])
# pok3 = Pokemon("Peter", ['Dormant'])
# pok4 = Pokemon("Lita", ['Distressed', 'normal'])
# print(get_by_type([pok1, pok3, pok2, pok4], 'normal'))

# Test get_evolutionary_line method
# pok1 = Pokemon("Pikachu", ['Electric', 'dynamic', 'normal'])
# pok2 = Pokemon("Mucho", ['dynamic'], pok1)
# pok3 = Pokemon("Peter", ['Dormant'], pok2)
# pok4 = Pokemon("Lita", ['Distressed', 'normal'], pok3)

# print("Pok1 evol: ", get_evolutionary_line(pok1))
# print("Pok3 evol: ", get_evolutionary_line(pok3))
# print("Pok4 evol: ", get_evolutionary_line(pok4))
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
