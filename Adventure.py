import time

# Game Data
rooms = {
    "hallway": {
        "description": "You are in the hallway. There are doors to the left and right.",
        "options": {
            "left": "library",
            "right": "kitchen"
        }
    },
    "library": {
        "description": "You are in the library. It's quiet and filled with books.",
        "options": {
            "back": "hallway"
        },
        "items": ["key"]
    },
    "kitchen": {
        "description": "You are in the kitchen. There is food on the counter.",
        "options": {
            "back": "hallway"
        },
        "items": ["map"]
    }
}

inventory = []  # List to hold the items the player collects
current_room = "hallway"  # Starting point

def print_slow(text, delay=0.05):
    """Function to print text with a delay for a slow, dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_room(room):
    """Displays the room's description and available options."""
    print_slow(rooms[room]["description"])
    if "items" in rooms[room]:
        if rooms[room]["items"]:
            print_slow("You see the following items:", 0.1)
            for item in rooms[room]["items"]:
                print_slow(f"- {item}")
    print_slow("Available options:")
    for direction, next_room in rooms[room]["options"].items():
        print_slow(f"- {direction}: Go to the {next_room}")

def get_choice():
    """Prompts the player to make a choice."""
    while True:
        choice = input("What will you do? ").strip().lower()
        if choice in ["left", "right", "back"]:
            return choice
        print("Invalid choice. Please choose 'left', 'right', or 'back'.")

def handle_item(room):
    """Handles item collection."""
    if "items" in rooms[room] and rooms[room]["items"]:
        print_slow(f"You pick up the {rooms[room]['items'][0]}.")
        inventory.append(rooms[room]["items"].pop(0))
    else:
        print_slow("There is nothing to collect here.")

def check_inventory():
    """Displays the player's inventory."""
    if inventory:
        print_slow("Your inventory contains:")
        for item in inventory:
            print_slow(f"- {item}")
    else:
        print_slow("Your inventory is empty.")

def main():
    global current_room

    print_slow("Welcome to the College Dorm Adventure Game!")
    print_slow("You find yourself in a mysterious dorm with rooms to explore. Your goal is to gather the necessary items and escape.")

    # Main game loop
    while True:
        show_room(current_room)
        choice = get_choice()

        if choice in rooms[current_room]["options"]:
            current_room = rooms[current_room]["options"][choice]
        elif choice == "back":
            # Go back to the previous room
            if current_room == "library":
                current_room = "hallway"
            elif current_room == "kitchen":
                current_room = "hallway"
            print_slow("You head back to the hallway.")
        
        handle_item(current_room)
        check_inventory()

        # Check if player can escape (e.g., if they have the key and map)
        if "key" in inventory and "map" in inventory:
            print_slow("You have collected the key and the map! You can now escape the dorm.")
            break  # End the game

        time.sleep(1)

    print_slow("Congratulations! You have escaped the dorm. Thanks for playing!")

# Start the game
if __name__ == "__main__":
    main()

