# College-Dorm-Adventure
### Game Concept:
The player finds themselves in a mysterious college dorm and needs to explore various rooms, gather items, and solve simple puzzles to escape. 

### Game Breakdown:
Rooms and Choices:
The game uses a dictionary (rooms) to store information about each room, including the description, available options (which room to go next), and items present in the room.
### Player Inventory:
The player's inventory is stored in a list called inventory. The player can collect items such as a key and map.
### Features of the Game:
Exploration: The player navigates between different rooms (library, kitchen, hallway).
Item Collection: The player can collect items (key, map) and store them in their inventory.
Simple Puzzles: The game requires the player to collect the key and map before they can escape.

### Functions:
print_slow: Prints text slowly for dramatic effect, enhancing the storytelling.
show_room: Displays the description of the current room and the available options.
get_choice: Prompts the player for an input (direction to go).
handle_item: If the player is in a room with items, it adds the item to their inventory.
check_inventory: Shows the player's current inventory.
### Conditionals and Loops:

Conditionals are used to handle different actions based on the player's choice (e.g., going left, right, or back).
Loops are used in main() to continually update the game state and allow the player to keep exploring until they collect the necessary items and escape.

### Ending Condition:
The game ends when the player collects both the key and map, which are required to escape the dorm.
