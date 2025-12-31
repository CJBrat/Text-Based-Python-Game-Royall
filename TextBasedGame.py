#caylie Royall- Text based game

def showInstructions():
    print('Collect 6 items to win the game, or get eaten by the zombie hoard.')
    print('Directions: forward, back, left, right')

def showHelp():
    print("Here are some possible commands:")
    print("'[direction]' - Move in a specific direction.")
    print("'pick up item' - Pick up an item in the current room.")
    print("'use item' - Use an item in your inventory")
    print("'inspect item' - Inspect an item in the room and find out what your character has to say about it.")
    print("'save' - save your game!")
    print("'load' - load your game!")
    print("'check inventory' - Check your current inventory.")
    print("'help' - Display this help message.")
    print("'exit' - End the game.")

def saveGame(current_room, inventory):
    with open('savegame.txt', 'w') as file:
        file.write(f"{current_room}\n")
        file.write(','.join(inventory))

def move_player(current_room, direction, rooms):
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print(f'You move {direction} to the {current_room}.')
        if check_for_item(current_room, rooms):
            print(f"There's a {rooms[current_room]['item']} in this room.")
    else:
        print("That direction is invalid.")
    return current_room

def get_item(current_room, item_name, inventory, rooms):
    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        inventory.append(item)
        del rooms[current_room]['item']
        print(f"You collected the {item}!")
    else:
        print("There are no items to collect in this room.")

def check_for_item(current_room, rooms):
    if 'item' in rooms[current_room]:
        return True
    else:
        return False

def inspect_item(current_room, rooms):
    if 'item' in rooms[current_room]:
        item_name = rooms[current_room]['item']
        item_description = rooms[current_room].get('item_description', 'You see nothing special about this item.')
        character_message = rooms[current_room].get('character_message', 'You feel intrigued by this item.')
        print(f"You inspect the {item_name}: {item_description}")
        print(f"Character says: '{character_message}'")
    else:
        print("There are no items to inspect in this room.")

def use_item(item_name, inventory):
    if item_name.lower() in [item.lower() for item in inventory]:
        if item_name.lower() == 'flashlight':
            print("You turn on the flashlight and the rooms are more illuminated now.")
            # Add any effects or changes to the game state related to using the flashlight
        elif item_name.lower() == 'medications':
            print("You take the medications and feel slightly better.")
            # Add any effects or changes to the game state related to using the medications
        # Add more conditions for other items as needed
        else:
            print("You cannot use this item.")
    else:
        print("You don't have that item in your inventory.")

def loadGame():
    try:
        with open('savegame.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                current_room = lines[0].strip()
                inventory = lines[1].strip().split(',')
                return current_room, inventory
            else:
                print("Invalid savegame.txt format. It should contain at least two lines.")
                return None, None
    except FileNotFoundError:
        print("No saved game found.")
        return None, None

def main():
    rooms = {
        'Entrance': {'description': 'You enter a small room with a small rug and a little table with some decorations\n'
                                    ' that are destroyed and what seemed to be a key bowl on top of it.',
                     'forward': 'Livingroom'},
        'Livingroom': {
            'description': 'It is dimly lit with 2 couches in the shape of an L.\n '
                           'There is a small coffee table on a small rug in front of the couches and a tv that seems as\n'
                           'though it is attached to the wall with a wall mount.\n'
                           'It looks like someone tried to yank it off the wall so it is tilted with a blood\n'
                           'smear next to it.\n'
                           'You also notice some crooked or broken picture frames on the floor and hanging up on the wall.\n'
                           'On the coffee table you see a radio and it still works as it is making white noise.',
                    'forward': 'Bedroom', 'back': 'Entrance', 'left': 'Office', 'right': 'Dining room', 'item': 'Radio', 'item_description': 'A radio AKA a Walkie.', 'character_message': 'A radio, I could bring this back incase the camp finds another one!'},
        'Dining room': {'description': 'There is a large table in the center surrounded\n'
                                       'by 6 chairs and a small china cabinet. Maybe it is worth looking at!',
                    'left': 'Livingroom', 'forward': 'Kitchen', 'item': 'Flashlight', 'item_description': 'A sturdy flashlight that emits a bright beam of light.', 'character_message': 'At least it works, I am glad I found this flashlight, the darkness does not seem as threatening anymore.'},
        'Office': {'description': 'There are scattered papers and an old desk and a half broken\n'
                                  'bookshelf where it looks like a fight had ensued. You also notice a puddle of blood\n'
                                  'on the floor and smears all over the wall but there is no source to all the blood.\n'
                                  'That is curious, there is something taped under the desk!',
                   'right': 'Livingroom', 'item': 'Ruger', 'item_description': 'A semi-automatic pistol, seems to be loaded.', 'character_message': 'Alright! This is awesome and there is even ammo with it! This gun gives me some sense of security, but I hope I will not have to use it.'},
        'Kitchen': {'description': 'It smells of decay and there are cockroaches scuttling about.',
                    'left': 'Bedroom', 'back': 'Dining room', 'forward': 'Basement', 'item': 'Canned foods', 'item_description': 'A bunch of canned foods, the labels are faded.', 'character_message': 'Well I will be damned, that is a lot of food. Hopfully it will last me and my camp a while.'},
        'Basement': {'description': 'It is dark and damp, with crates stacked against the walls.',
                    'back': 'Kitchen', 'item': 'Hoard'},
        'Bedroom': {'description': 'The bed is unmade and there are clothes strewn about.\n'
                                   'There is a queen sized bed in the middle of the wall and 2 small dressers on the\n'
                                   'wall accross from the bed.',
                    'back': 'Livingroom', 'forward': 'Bathroom', 'right': 'Kitchen', 'item': 'Clothes', 'item_description': 'There are quite a few sizes, enough for a small family', 'character_message': 'Yes! Now I can help the children back at camp and I do not have to wear the same clothes every damn day!'},
        'Bathroom': {'description': 'The mirror is cracked and there is a faint odor of mildew.',
                    'back': 'Bedroom', 'item': 'Medications', 'item_description': 'Different types of medications, all have a different use.', 'character_message': 'Jiminy Cricket! I have found the motherlode! Maybe I will take some now for the amount of pain I am in.'},

        'Exit': {'description': 'Congratulations! You have escaped the abandoned house.'}

    }
    current_room = 'Entrance'
    inventory = []
    visited_rooms = {room: False for room in rooms}  # Initialize all rooms as not visited

    print("Welcome to the Zombie Text Survival Game!")
    showInstructions()
    showHelp()
    print("Type 'exit' to end the game.")
    print()

    while current_room != 'Exit':
        if not visited_rooms[current_room]:  # Check if the room has not been visited
            print(rooms[current_room]['description'])
            visited_rooms[current_room] = True  # Mark the room as visited
        print("You are in the", current_room)
        direction = input(
            "Enter direction to move (forward, back, left, right), 'pick up item' to pick up an item, or 'Check inventory' to see your inventory: ").lower()
        print('-' * 50)  # Print a line of dashes

        if direction == 'exit':
            current_room = 'Exit'
        elif direction.startswith('use '):
            item_name = direction[4:]  # Extract the item name from the command
            use_item(item_name, inventory)
            print('-' * 50)
        elif direction == 'load':
            current_room, inventory = loadGame()
            if current_room:
                print("Game loaded successfully.")
        elif direction == 'help':
            showHelp()
        elif direction == 'save':
            saveGame(current_room, inventory)
            print("Game saved.")
        elif direction == 'inspect item':
            inspect_item(current_room, rooms)
            continue
        else:
            if direction in ['forward', 'back', 'left', 'right']:
                current_room = move_player(current_room, direction, rooms)
                if current_room == 'Basement' and len(inventory) < 6:
                    print(
                        "You cannot enter the Basement without collecting all 6 items. The zombie hoard overwhelmed and ate you. You lose!")
                    current_room = 'Exit'  # End the game
            elif direction == 'pick up item' and 'item' in rooms[current_room]:
                item_name = rooms[current_room]['item']
                if item_name == 'Hoard':
                    print("You cannot collect the hoard. It's too dangerous!")
                else:
                    get_item(current_room, item_name, inventory, rooms)

                    if len(inventory) == 6:
                        print(
                            "Congratulations! You have collected all 6 items and defeated the zombie hoard. You win!")
                        current_room = 'Exit'
            elif direction == 'check inventory':
                print("Your inventory:", inventory)
            else:
                print("Invalid command. Please enter a valid direction, 'exit', 'pick up item', or 'Check inventory'.")
        print()

    print("Thank you for playing the Zombie Text Survival Game!")


if __name__ == "__main__":
    main()