from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(room['outside'])
current_room = player.room     #current room = outside

room['foyer'].add_item(Item('Sword'))
room['overlook'].add_item(Item('Golf Tee'))
room['narrow'].add_item(Item('Garbage Can'))
room['treasure'].add_item(Item('The Crystal Skull'))

def wrong_way():
    print('movement is not allowed')

in_game = True

while in_game == True:
    print(str(current_room))

    loot = ''
    for i in current_room.loot:
        loot += f'{i.name}'
    print('Loot: ' + loot)

    bag = ''
    for i in player.bag:
        bag += f'{i.name}'
    print('Bag: ' + bag)

    move = input('Where would you like to go? (North, South, East, or West) : ')
    split_move = move.split()

    if len(split_move) == 1:
 
        if move == 'North':
            if current_room.n_to is None:
                wrong_way()
            else:
                current_room = current_room.n_to

        elif move == 'South':
            if current_room.s_to is None:
                wrong_way()
            else:
                current_room = current_room.s_to

        elif move == 'East':
            if current_room.e_to is None:
                wrong_way()
            else:
                current_room = current_room.e_to

        elif move == 'West':
            if current_room.w_to is None:
                wrong_way()
            else:
                current_room = current_room.w_to

        elif move == 'q':
            in_game = False

        else:
            print(f'{move} is not an option')

    elif len(split_move) == 2:

        print(loot, split_move[1], 'what will it return')

        # will only work with one item in loot, use index() and find away to get loot in a list of names
        if loot == split_move[1]:
            print('item found')

            if split_move[0] == 'get':
                player.add_item(Item(split_move[1]))

            elif split_move[0] == 'drop':
                print('drop')

        else:
            print('not found')



        # else:
        #     print('not an option')



