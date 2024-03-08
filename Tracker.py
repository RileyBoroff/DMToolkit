import os

message = ""
round_num = 1

def create_initiatives(initiatives):
    for _ in range(num_things):
        name = str_checker("Enter the name for NPC/player: ")
        initiative = int_checker(f"Enter the initiative for {name}: ")
        armor_class = int_checker(f"Enter Armor Class relative to {name}: ")
        hit_points = int_checker(f"Enter Hit Points relative to {name}: ")
        initiatives[name] = {'initiative': initiative, 'armor_class': armor_class, 'hit_points': hit_points, 'status_effects': []}  # Initialize 'status_effects' as an empty list
    return initiatives

def str_checker(prompt):
    while True:
        user_input = input(prompt)
        if isinstance(user_input, str):
            return user_input
        else:
            print("Please enter a valid string")

def int_checker(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number")

def damage(initiatives, name, amount):
    global message
    if name in initiatives:
        initiatives[name]['hit_points'] -= amount
        if initiatives[name]['hit_points'] <= 0:
            message = f"{name} has fallen to 0 hp"
            initiatives[name]['hit_points'] = 0  # Fixed the assignment here
        else:
            message = f"{name}'s HP reduced by {amount} currently at {initiatives[name]['hit_points']}."
    else:
        message = f"No NPC or player named {name} found in the initiatives list."

import os

def show_initiatives(sorted_initiatives, current_index):
    global round_num
    increment_round = False  # Initialize flag to determine if round_num should be incremented
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Round: {round_num}")
    for index, (name, data) in enumerate(sorted_initiatives, start=1):
        status_effects = [effect['effect_name'] for effect in data.get('status_effects', [])]  # Extract status effects
        status_effects_str = ', '.join(status_effects) if status_effects else "None"  # Join status effects if they exist, otherwise, print "None"

        # Modify the printing logic to include duration for each effect
        effect_info = []
        for effect in data.get('status_effects', []):
            effect_info.append(f"{effect['effect_name']} ({effect['duration']} rounds)")
        effect_info_str = ', '.join(effect_info) if effect_info else "None"

        if index == current_index:
            print(f"* {name}: AC: {data['armor_class']}, HP: {data['hit_points']}, Status Effects: {effect_info_str}")
        else:
            print(f" {name}: AC: {data['armor_class']}, HP: {data['hit_points']}, Status Effects: {effect_info_str}")

        if current_index == 1:
            increment_round = True  # Set flag to True if current_index is 1

    return increment_round  # Return the flag to indicate whether round_num should be incremented

def remove_from_initiative(initiatives, name):  # Added initiatives and name as arguments
    global message
    if name in initiatives:
        del initiatives[name]
        return initiatives, True  # Return the updated initiatives dictionary and a boolean indicating success
    else:
        message = f"No NPC or player named {name} found in the initiatives list."
        return initiatives, False  # Return the unchanged initiatives dictionary and a boolean indicating failure

def status_counter(initiatives):
    for name, data in initiatives.items():
        for effect in data['status_effects']:
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                data['status_effects'].remove(effect)
    return initiatives

def add_status_effect(initiatives):
    global message
    name = str_checker("Enter the name of the NPC/player to add status effect to: ")  # Added name assignment
    if name in initiatives:
        effect_name = input("Enter the name of the effect: ")
        duration = int_checker("Enter the duration of the effect (in rounds): ")
        initiatives[name]['status_effects'].append({'effect_name': effect_name, 'duration': duration})
        message = f"Added {effect_name} to {name} for {duration} rounds."
    else:
        message = f"No NPC or player named {name} found in the initiatives list."
def remove_status_effect(initiatives):
    global message
    name = str_checker("Enter the name of the NPC/player to remove a status effect from: ")
    if name in initiatives:
        effect_name = str_checker("Enter the name of the effect to remove: ")
        # Check if the effect exists in the list of status_effects
        for effect in initiatives[name]['status_effects']:
            if effect['effect_name'] == effect_name:
                initiatives[name]['status_effects'].remove(effect)
                message = f"Removed {effect_name} from {name}."
                break  # Exit loop once the effect is removed
        else:
            message = f"No effect named {effect_name} found for {name}."
    else:
        message = f"No NPC or player named {name} found in the initiatives list."

initiatives = {}
num_things = int_checker("Enter the number of NPCs/players included in this initiative: ")
initiatives = create_initiatives(initiatives)
sorted_initiatives = sorted(initiatives.items(), key=lambda x: x[1]['initiative'], reverse=True)
current_index = 1

while True:
    show_initiatives(sorted_initiatives, current_index)
    print(message)
    action = input("Enter an action (d: deal damage, n: next, h: help, s add a status effect, s- remove a status effect, exit: exit)\n: ")

    if action == "d":
        name = str_checker("Enter the name of NPC/player to deal damage to: ")  # Added name assignment
        amount = int_checker("Enter the amount of damage: ")
        damage(initiatives, name, amount)

    elif action == "n":
        current_index = (current_index % len(sorted_initiatives)) + 1
        status_counter(initiatives)
        # Example usage
        increment_round = show_initiatives(sorted_initiatives, current_index)
        if increment_round:
            round_num += 1

    elif action == "+":
        initiatives = create_initiatives(initiatives)
        sorted_initiatives = sorted(initiatives.items(), key=lambda x: x[1]['initiative'], reverse=True)

    elif action == "-":
        name = str_checker("Enter the name of the NPC/player to remove: ")  # Added name assignment
        initiatives, removed = remove_from_initiative(initiatives, name)
        if not removed:
            message = f"No NPC or player named {name} found in the initiatives list."
        sorted_initiatives = sorted(initiatives.items(), key=lambda x: x[1]['initiative'], reverse=True)

    elif action == "h" or action == "help":
        try:
            with open('help.txt', 'r') as file:
                file_contents = file.read()
                print(file_contents)
        except FileNotFoundError:
            print("The help file was not found.")

    elif action == "s":
        add_status_effect(initiatives)
    elif action =="s-":
        remove_status_effect(initiatives)

    elif action == "exit":
        break
    elif action == "":
        print("Please enter a vaid command")

    else:
        print("Invalid input")
