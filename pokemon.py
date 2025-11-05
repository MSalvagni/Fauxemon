import random
import time

class Pokemon:
    #These are the attributes that can be stores by the pokemon 
    #Can add moves, speed, defense, or whatever else
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"
    
    def take_damage(self, amount):
        self.hp = max(0,self.hp - amount)

    def is_fainted(self):
        return self.hp <= 0

def ask_name():    
    player = input("What is your name? ")
    print(f"Your name is {player}")


    while True:
        first_answer = input("Is that right? (y/n) ")
        if first_answer == "y":
            return player
        elif first_answer == "n":
            player = input("What is your name? ")
            print(f"Your name is {player}")
        else:
            print("Enter a valid answer")

def choose_starter():
    pokemons = [
        Pokemon("Bulbasaur", 45),
        Pokemon("Charmander", 39),
        Pokemon("Squirtle", 44)
        ]

    type_advantage = {
        "Bulbasaur": "Charmander",
        "Charmander": "Squirtle",
        "Squirtle": "Bulbasaur"
    }

    print("Choose your starter Pokemon")
    for i, poke in enumerate(pokemons, start=1):
        print(f"{i}) {poke.name}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in ["1", "2","3"]:
            chosen_pokemon = pokemons[int(choice) -1]

            #Confirmation loop
            while True:
                confirm = input(f"Are you sure about {chosen_pokemon}? (y/n) " )
                if confirm == "y":
                    print(f"You chose {chosen_pokemon.name}!")
                    time.sleep(1)
                    rival_choice = type_advantage[chosen_pokemon.name]
                    rival_pokemon = next(p for p in pokemons if p.name == rival_choice)
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

def take_turn(attacker, defender):
    damage = random.randint(5, 10)
    defender.take_damage(damage)
    print(f"{attacker.name} attacks! {defender.name} loses {damage} HP")
    time.sleep(1)
    print(f"{defender.name} has {defender.hp} HP left!\n")
    time.sleep(1)


def battle(player_pokemon, rival_pokemon):
    print(f"Battle is about to begin between your {player_pokemon.name} and your rival's {rival_pokemon.name}")
    time.sleep(1)

    while not player_pokemon.hp == 0 and not rival_pokemon.hp == 0:
        print(f"Your pokemon: {player_pokemon}")
        print(f"Rival's pokemon: {rival_pokemon}\n")
        action = input("Choose your action:\n1) Attack\n")
        if action == "1":
            take_turn(player_pokemon, rival_pokemon)
        else:
            print("Make a valid choice")
            continue


        #Check if a pokemon faints
        if rival_pokemon.hp == 0:
            print(f"{rival_pokemon.name} has fainted. You won the battle!")
            break

        take_turn(rival_pokemon, player_pokemon)

        if player_pokemon.hp == 0:
            print(f"Your pokemon fainted!")
            break


def start_game():
    player_name = ask_name()
    print(f"Welcome Trainer, {player_name}")
    player_pokemon, rival_pokemon = choose_starter()
    time.sleep(1)
    battle(player_pokemon, rival_pokemon)


start_game()