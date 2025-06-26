class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def print_pokemon(self):
        print('{\n \"name\": \"',self.name,'\"\n', '\"types\": ',self.types,'\n','\"is_caught\": \"',self.is_caught,'\"\n','}')
    
    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(self.name, " I choose you!")
        else:
            print(self.name, " is wild! You can try and catch them.")
        
    def add_type(self, type):
        self.types.append(type)

# my_pokemon = Pokemon("Pikachu", ["Electric"], False)
# my_pokemon.print_pokemon()
# my_pokemon.choose()

# my_pokemon.is_caught = True
# my_pokemon.print_pokemon()
# my_pokemon.choose()

# my_pokemon.add_type("Dynamic")
# my_pokemon.print_pokemon()