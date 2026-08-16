"""
John will be always the player
Jack always the bot

conditions du bot

perdant :
pencils % 5 == 4
pencils == 1

gagnant :
pencils % 4 == 0 (prendra 3 crayons)
pencils % 3 == 4 (prendra 2 crayons)
pencils % 4 == 2 (prendra 1 crayon)

"""
import random

def robot_turn(number_pens):
    if number_pens % 4 == 2:
        robot_choice = 1
        return robot_choice
    elif number_pens % 2 == 1:
        if number_pens == 1:
            robot_choice = 1
            return robot_choice
        else:
            robot_choice = 2
            return robot_choice
        robot_choice = 2
        return robot_choice
    elif number_pens % 4 == 0 :
        robot_choice = 3
        return robot_choice
    else:
        robot_choice = random.randint(1, 3)
        return robot_choice

start_number = input("How many pencils would you like to use:")

def numeric_number(start_number):
    try:
        int(start_number)
        return True
    except ValueError:
        return False

def positif_number(start_number):
    if start_number <= 0:
        return False
    else:
        return True

while True:
    if not numeric_number(start_number):
        print("The number of pencils should be numeric")
        start_number = input()
        numeric_number(start_number)
    else:
        start_number = int(start_number)
        if not positif_number(start_number):
            print("The number of pencils should be positive")
            start_number = input()
            if not numeric_number(start_number):
                print("The number of pencils should be numeric")
                start_number = input()
                numeric_number(start_number)
            else:
                start_number = int(start_number)
        else:
            start_number = int(start_number)
            break


number_pens = start_number

player_turn = input("Who will be the first (John, Jack):")

while True:
    if player_turn not in ["Jack", "John"]:
        print("Choose between 'John' and 'Jack'")
        player_turn = input("Who will be the first (John, Jack):")
    else:
        break

turn_state = player_turn

print(f"{"|" * number_pens}")

### Zone de fonctions

#fonction pour vérifier si le joueur ne prend que 1, 2 ou 3 crayons
def check_number_pens():
    pencil_change = input()
    while True:
        if pencil_change not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            pencil_change = input()
        else:
            return int(pencil_change)

#Modifie le nombre de crayons en jeu
def result_of_choice(pencil_change: int, number_pens: int):     #Cette fonction fonctionne
    number_pens -= int(pencil_change)
    return number_pens

#Check de l'état du jeu en cours
def game_status(number_pens):
    """
    je dois chequer l'état du jeu en cours
    True = le jeu continue
    False = Le jeu s'arrête
    """
    pencil_change = check_number_pens()
    if number_pens > 3:
        return int(pencil_change)
    elif 3 >= number_pens > 0:
        while True:
            if pencil_change > number_pens:
                print("Too many pencils were taken")
                pencil_change = input()
                return int(pencil_change)
            else:
                return int(pencil_change)


#Boucle qui tourne tant qu'il y a des crayons en jeu
while True:
    if player_turn == "John":
        print(f"{player_turn}\'s turn:")

        pencil_change = game_status(number_pens)
        number_pens = result_of_choice(pencil_change, number_pens)      # Applique le résultat du tour de jeu
        print(f"{"|" * number_pens}")

        player_turn = "Jack"
        if number_pens == 0:
            print(f"{player_turn} won!")
            break
        else:
            continue

    else:
        print(f"{player_turn}\'s turn:")

        #pencil_change = check_number_pens()
        pencil_change = robot_turn(number_pens)
        print(pencil_change)
        number_pens = result_of_choice(pencil_change, number_pens)        # Applique le résultat du tour de jeu
        print(f"{"|" * number_pens}")

        player_turn = "John"
        if number_pens == 0:
            print(f"{player_turn} won!")
            break
        else:
            continue
