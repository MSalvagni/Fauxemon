import random
import time


class Pokemon:
    #These are the attributes that can be stores by the pokemon 
    #Can add moves, speed, defense, or whatever else
    def __init__(self, name, hp, max_hp, moves, speed, level, xp):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.moves = moves
        self.speed = speed
        self.level = level
        self.xp = xp
        self.xp_to_next_lvl = 30 * level

    def __str__(self):
        return f"{self.name} (HP: {self.hp}) (LVL:{self.level}) ({self.xp}/{self.xp_to_next_lvl}XP)"
    
    def take_damage(self, amount):
        self.hp = max(0,self.hp - amount)

    def gain_xp(self, amount):
        print(f"{self.name} gained {amount} XP!")
        self.xp += amount
        
        while self.xp >= self.xp_to_next_lvl:
            self.xp -= self.xp_to_next_lvl
            self.level += 1
            self.xp_to_next_lvl = 30 * self.level
            print(f"{self.name} leveled up to {self.level}!")

            hp_increase = 5
            self.max_hp += hp_increase 

            self.hp = self.max_hp
            print(f"HP: {self.max_hp}")



moves = {
    "Tackle":(5, 10, 90),
    "Vine Whip": (8, 12, 90),
    "Ember": (8, 12, 90),
    "Water Gun": (8, 12, 90)
}
    


def ask_name():    
    player = input("What is your name? ")
    print(f"Your name is {player}")


    while True:
        answer = input("Is that right? (y/n) ").lower()
        if answer == "y":
            return player
        elif answer == "n":
            player = input("What is your name? ")
            print(f"Your name is {player}")
        else:
            print("Enter a valid answer")

def choose_starter():
    pokemons = [
        Pokemon("Bulbasaur", 45, 45, ["Tackle", "Vine Whip"], 45, 1, 0),
        Pokemon("Charmander", 39, 39, ["Tackle", "Ember"], 65, 1, 0),
        Pokemon("Squirtle", 44, 44, ["Tackle", "Water Gun"], 43, 1, 0)
        ]

    type_advantage = {
        "Bulbasaur": "Charmander",
        "Charmander": "Squirtle",
        "Squirtle": "Bulbasaur"
    }
    
    #store pokemon for faster lookup
    pokemon_dict = {p.name: p for p in pokemons}

    print("Choose your starter Pokemon")
    for i, poke in enumerate(pokemons, start=1):
        print(f"{i}) {poke.name}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in ["1", "2","3"]:
            chosen_pokemon = pokemons[int(choice) -1]

            #Confirmation loop
            while True:
                confirm = input(f"Are you sure about {chosen_pokemon}? (y/n) " ).lower()
                if confirm == "y":
                    print(f"You chose {chosen_pokemon.name}!")
                    time.sleep(1)
                    rival_choice = type_advantage[chosen_pokemon.name]
                    rival_pokemon = pokemon_dict[rival_choice]
                    print(f"Your rival has chosen {rival_pokemon.name}.")
                    time.sleep(1)
                    return chosen_pokemon, rival_pokemon  
                elif confirm == "n":
                    print("Okay, pick again.")
                    break
                else:
                    print("Make a valid choice")
        else:
            print("Make a valid choice")

def take_turn(attacker, defender, move_name):
    low, high, accuracy = moves[move_name]
    if random.randint(1, 100) <= accuracy:
        damage = random.randint(low, high)
        defender.take_damage(damage)
        print(f"{attacker.name} attacks with {move_name}! {defender.name} loses {damage} HP")
        time.sleep(1)
        print(f"{defender.name} has {defender.hp} HP left!\n")
        time.sleep(1)
    else:
        print(f"{attacker.name}'s attack missed!")

def battle(player_pokemon, rival_pokemon):
    is_Trainer = True
    print(f"Battle is about to begin between your {player_pokemon.name} and your rival's {rival_pokemon.name}")
    time.sleep(1)
    did_win = False

    while player_pokemon.hp > 0 and rival_pokemon.hp > 0:
        print(f"Your pokemon: {player_pokemon.name} HP:{player_pokemon.hp}")
        print(f"Rival's pokemon: {rival_pokemon.name} HP:{rival_pokemon.hp}\n")
        action = input("Choose your action:\n1) Attack\n2) Flee\n>")
        #pick which move to use
        if action == "1":
            print("Choose a move:")
            for i, move in enumerate(player_pokemon.moves, start=1):
                print(f"{i}) {move}")

            choice = int(input(">")) - 1
            chosen_move = player_pokemon.moves[choice]

            rival_move = random.choice(rival_pokemon.moves)
            ## turn based system with speed. seems not optimal..
            if player_pokemon.speed >= rival_pokemon.speed:
                take_turn(player_pokemon, rival_pokemon, chosen_move)
                if rival_pokemon.hp <= 0:
                    print(f"Rival's {rival_pokemon.name} has fainted")
                    did_win = True
                    break
                take_turn(rival_pokemon, player_pokemon, rival_move)
                if player_pokemon.hp <= 0:
                    print(f"Your {player_pokemon.name} has fainted!")
                    break
            else:
                take_turn(rival_pokemon, player_pokemon, rival_move)
                if player_pokemon.hp <= 0:
                    print(f"Your {player_pokemon.name} fainted!")
                    break
                take_turn(player_pokemon, rival_pokemon, chosen_move)
                if rival_pokemon.hp <= 0:
                    print(f"Rival's {rival_pokemon.name} has fainted!")
                    did_win = True
                    break
    
        elif action == "2":
            if is_Trainer == True:
                print("Can't escape from trainer battles")
            else:
                print("Got Away Safely!")
                break
        else:
            print("Make a valid choice")
            continue

    if did_win:
        player_pokemon.gain_xp(30)

def start_game():
    player_name = ask_name()
    print(f"Welcome Trainer, {player_name}")
    player_pokemon, rival_pokemon = choose_starter()
    time.sleep(1)
    battle(player_pokemon, rival_pokemon)


start_game()