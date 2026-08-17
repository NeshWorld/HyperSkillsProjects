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
    elif number_pens % 4 == 0 :
        robot_choice = 3
        return robot_choice
    else:
        robot_choice = random.randint(1, 3)
        return robot_choice


# Basically... Get an input
def get_input():
    return input("How many pencils would you like to use:")

# Verify if the input is numeric or not
def numeric_number(start_number):
    try:
        int(start_number)
        return True
    except ValueError:
        print("The number of pencils should be numeric")
        return False

# Verify if the number is positive or not
def positive_number(start_number):
    if int(start_number) <= 0:
        print("The number of pencils should be positive")
        return False
    else:
        return True

start_number = get_input()

while True:
    if not numeric_number(start_number):
        start_number = get_input()
    elif not positive_number(start_number):
        start_number = get_input()
    else:
        break


number_pens = int(start_number)

player_turn = input("Who will be the first (John, Jack):")

while True:
    if player_turn not in ["Jack", "John"]:
        print("Choose between 'John' and 'Jack'")
        player_turn = input("Who will be the first (John, Jack):")
    else:
        break

turn_state = player_turn

print(f"{"|" * number_pens}")

### Functions area

# Verify if the player takes only 1, 2 or 3 pencils
def check_number_pens():
    pencil_change = input()
    while True:
        if pencil_change not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            pencil_change = input()
        else:
            return int(pencil_change)

# Modify the number of pencils in play
def result_of_choice(pencil_change: int, number_pens: int):     #This function works
    number_pens -= int(pencil_change)
    return number_pens

# Check the state of the game in progress
def game_status(number_pens):
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


# Loop that runs as long as there are pencils in play
while True:
    if player_turn == "John":
        print(f"{player_turn}\'s turn:")

        pencil_change = game_status(number_pens)
        number_pens = result_of_choice(pencil_change, number_pens)      # Apply the result of the game turn
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
        number_pens = result_of_choice(pencil_change, number_pens)        # Apply the result of the game turn
        print(f"{"|" * number_pens}")

        player_turn = "John"
        if number_pens == 0:
            print(f"{player_turn} won!")
            break
        else:
            continue
