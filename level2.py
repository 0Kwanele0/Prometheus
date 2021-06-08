import random
from sys import exit

# Defining initial variables
xp = 50
map2 = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0], [1, 1], [2, 1], [1, 2], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
        [4, 0],
        [4, 1], [4, 2], [4, 3], [4, 4], [2, 4], [1, 4], [0, 4],
        [0, 3], [1, 3], [2, 3]]

hero_position = [2, 2]

# Elements in the island
fire = 2
wolf = 4
fire_position = random.choice(map2)
wolf_position = random.choice(map2)
treasure_1 = random.choice(map2)
treasure_2 = random.choice(map2)
treasures = 3


# A function to be called when encountering fire or a wolf
# allowing the player to choose between fighting or running
def wolf_and_fire2():
    a = ['1', '2']
    b = ['RUN', 'FIGHT']
    for a, b in zip(a, b):
        print(a + "." + b)


# A function to be called when a player has to make a move
# allowing the player to choose direction
def choices2():
    a = ['1', '2', '3', '4', '5', '6', '7']
    b = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SAVE', 'LOAD', 'EXIT']
    for a, b in zip(a, b):
        print(a + "." + b)


# The game loop - level 1

def level():
    global wolf, fire, xp, treasures
    while fire > 0 or wolf > 0:
        print("\nXP:", xp)
        print("Your position:", hero_position)

        print("\nMake your a move:")
        choices2()

        move = input("\nMove: ")

        if move == "4":
            hero_position[0] += 1
            hero_position[1] += 0
            if hero_position in map2:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")
                elif wolf > 0 and (hero_position == wolf_position):
                    print("\nWOLF!!!\n")
                    wolf_and_fire2()
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
                    wolf_and_fire2()
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
            if hero_position in map2:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW!! you just found a TREASURE!!! and you got +20 xp.\n")
                elif wolf > 0 and (hero_position == wolf_position):
                    print("\nWOLF!!!\n")
                    wolf_and_fire2()
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
                    wolf_and_fire2()
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
            if hero_position in map2:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")

                elif wolf > 0 and (hero_position == wolf_position):
                    print("\nWOLF!!!!!!\n")
                    wolf_and_fire2()
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
                    wolf_and_fire2()
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
            if hero_position in map2:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")
                elif wolf > 0 and (hero_position == wolf_position):
                    print("\nWOLF!!!\n")
                    wolf_and_fire2()
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
                    wolf_and_fire2()
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
        elif move == "7":
            exit()
        else:
            print("\nPlease choose a valid move.")

    print("\n****-- Congratulations you have completed Level 1. --****")

