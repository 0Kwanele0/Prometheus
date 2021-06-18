# A module to place elements randomly in the island
import random
from level2 import level
from time import sleep

# Defining initial variables
xp = 50
map_x = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0], [1, 1], [2, 1], [1, 2], [2, 2]]
hero_position = [1, 1]

# Elements in the island
fire = 1
wolf = 1
fire_position = random.choice(map_x)
wolf_position = random.choice(map_x)
treasure_1 = random.choice(map_x)
treasure_2 = random.choice(map_x)
treasures = 2


# A function to be called when encountering fire or a wolf
# allowing the player to choose between fighting or running
def wolf_and_fire():

    a = ['1', '2']
    b = ['RUN', 'FIGHT']
    for a, b in zip(a, b):
        print(a + "." + b)


# A function to be called when a player has to make a move
# allowing the player to choose direction
def choices():
    a = ['1', '2', '3', '4']
    b = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    for a, b in zip(a, b):
        print(a + "." + b)


# This is a welcome message printed  when the game starts
print("\n-------WELCOME TO LEVE 1.----------")
print("\nWelcome to the beautiful game,\nYou are dropped in an island"
      " and your role is to survive.\n")
sleep(.3)
# The game loop - level 1


while fire > 0 or wolf > 0:
    print("\nXP:", xp)
    print("Your position:", hero_position)
    sleep(.3)
    print("\nMake your a move:")
    choices()

    move = input("\nMove: ")

    if move == "4":
        hero_position[0] += 1
        hero_position[1] += 0
        if hero_position in map_x:
            if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                xp += 20
                treasures -= 1
                print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")
            elif wolf > 0 and (hero_position == wolf_position):
                print("\nWOLF!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the wolf"
                          " is still in the island.")
                else:
                    print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                    xp -= 30
                    wolf -= 1
            elif fire > 0 and (hero_position == fire_position):
                print("\nFIRE!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the fire"
                          " is still in the island.")
                else:
                    print("\nWow! you have put out the fire, but you were injured and lost 25 xp.\n")
                    xp -= 25
                    fire -= 1
            else:
                print("\nThe is nothing here, lets keep moving.\n")
        else:
            print("\nHey don't fall in the ocean, try another move.")
            hero_position[0] -= 1
    elif move == "3":
        hero_position[0] -= 1
        hero_position[1] += 0
        if hero_position in map_x:
            if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                xp += 20
                treasures -= 1
                print("\nWOW!! you just found a TREASURE!!! and you got +20 xp.\n")
            elif wolf > 0 and (hero_position == wolf_position):
                print("\nWOLF!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the wolf"
                          " is still in the island.")
                else:
                    print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                    xp -= 30
                    wolf -= 1
            elif fire > 0 and (hero_position == fire_position):
                print("\nFIRE!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the fire"
                          " is still in the island.")
                else:
                    print("\nWow! you have put out the fire, but you were injured and lost 25 xp.\n")
                    xp -= 25
                    fire -= 1
                    print("XP:", xp)
                    print("Your position:", hero_position)
            else:
                print("\nThe is nothing here, lets keep moving.\n")
        else:
            print("\nHey don't fall in the ocean, try another move.")
            hero_position[0] += 1
    elif move == "2":
        hero_position[0] += 0
        hero_position[1] += 1
        if hero_position in map_x:
            if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                xp += 20
                treasures -= 1
                print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")

            elif wolf > 0 and (hero_position == wolf_position):
                print("\nWOLF!!!!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the wolf"
                          " is still in the island.")
                else:
                    print("\nWOW! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                    xp -= 30
                    wolf -= 1
            elif fire > 0 and (hero_position == fire_position):
                print("\nFIRE!!!!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the fire"
                          " is still in the island.")
                else:
                    print("\nWow! you have put out the fire, but you were injured and lost 25 xp.\n")
                    xp -= 25
                    fire -= 1
            else:
                print("\nThe is nothing here, lets keep moving.\n")
        else:
            print("\nHey don't fall in the ocean, try another move.")
            hero_position[1] -= 1
    elif move == "1":
        hero_position[0] += 0
        hero_position[1] -= 1
        if hero_position in map_x:
            if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                xp += 20
                treasures -= 1
                print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")
            elif wolf > 0 and (hero_position == wolf_position):
                print("\nWOLF!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the wolf"
                          " is still in the island.")
                else:
                    print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                    xp -= 30
                    wolf -= 1
            elif fire > 0 and (hero_position == fire_position):
                print("\nFIRE!!!\n")
                wolf_and_fire()
                f_or_r = input("Do you fight or you run: ")
                if f_or_r == "1":
                    print("\nBy running you have saved some xp, but the fire"
                          " is still in the island.")
                else:
                    print("\nWow! you have put out the fire, but you were injured and lost 25 xp.\n")
                    xp -= 25
                    fire -= 1
            else:
                print("\nThe is nothing here, lets keep moving.\n")
        else:
            print("\nHey don't fall in the ocean, try another move.")
            hero_position[1] += 1
    else:
        print("\nPlease choose a valid move.")

print("\n****-- Congratulations you have completed Level 1. --****")

action = input("\n1. Next level\n2. Replay\n3. Quit\nChoose: ")
if action == "1":
    print("\n-------WELCOME TO LEVE 2.----------")
    level()


