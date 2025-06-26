class Player:
    def __init__(self, character: str, kart: str, opponent = None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

def get_place(player: Player):
    res = 1

    # count opponents ahead
    opponent = player.ahead
    while opponent:
        res += 1
        opponent = opponent.ahead

    return res

# peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper", mario)

# print(get_place(peach))
# print(get_place(mario))
print(get_place(luigi))

    

    
