import random
from sys import exit

# Defining initial variables
from level2 import wolf_and_fire2

xp = 50
map3 = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0], [1, 1], [2, 1], [1, 2], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
        [4, 0],
        [4, 1], [4, 2], [4, 3], [4, 4], [2, 4], [1, 4], [0, 4],
        [0, 3], [1, 3], [2, 3], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [0, 6], [1, 6], [2, 6], [3, 6],
        [4, 6], [5, 6], [6, 6], [5, 0], [6, 0], [5, 1], [6, 1], [5, 2], [2, 2], [6, 3], [5, 3], [5, 4], [6, 4]]
run_count = 0
hero_position = [3, 3]

# Elements in the island
fire = 3
wolf = 6
treasures = 5

fire_position = random.choice(map3)
fire_position_1 = random.choice(map3)

wolf_position = random.choice(map3)
wolf_position_1 = random.choice(map3)

treasure_1 = random.choice(map3)
treasure_2 = random.choice(map3)


# A function to be called when encountering fire or a wolf
# allowing the player to choose between fighting or running
def wolf_and_fire3():
    a = ['1', '2']
    b = ['RUN', 'FIGHT']
    for a, b in zip(a, b):
        print(a + "." + b)


# A function to be called when a player has to make a move
# allowing the player to choose direction
def choices3():
    a = ['1', '2', '3', '4', '5', '6', '7']
    b = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SAVE', 'LOAD', 'EXIT']
    for a, b in zip(a, b):
        print(a + "." + b)


# The game loop - level 1

def bonus():
    global wolf, fire, xp, treasures, run_count
    while fire > 0 or wolf > 0:
        print("\nXP:", xp)
        print("Your position:", hero_position)
        print("\nMake your a move:")
        choices3()

        move = input("\nMove: ")

        if move == "4":
            hero_position[0] += 1
            hero_position[1] += 0
            if hero_position in map3:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")
                elif wolf > 0 and (hero_position == wolf_position or hero_position == wolf_position_1):
                    print("\nWOLF!!!\n")
                    wolf_and_fire2()
                    f_or_r = input("Do you fight or you run: ")
                    if f_or_r == "1":
                        print("\nBy running you have saved some xp, but the wolf"
                              " is still in the island.")
                        run_count += 1
                        if run_count == 3:
                            print("\nWATCH behind you, The WOLF!!!")
                            print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                            xp -= 30
                            wolf -= 1
                        else:
                            continue
                    else:
                        print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                        xp -= 30
                        wolf -= 1
                elif fire > 0 and (hero_position == fire_position or hero_position == fire_position_1):
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
            if hero_position in map3:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW!! you just found a TREASURE!!! and you got +20 xp.\n")
                elif wolf > 0 and (hero_position == wolf_position or hero_position == wolf_position_1):
                    print("\nWOLF!!!\n")
                    wolf_and_fire2()
                    f_or_r = input("Do you fight or you run: ")
                    if f_or_r == "1":
                        print("\nBy running you have saved some xp, but the wolf"
                              " is still in the island.")
                        run_count += 1
                        if run_count == 3:
                            print("\nWATCH behind you, The WOLF!!!")
                            print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                            xp -= 30
                            wolf -= 1
                        else:
                            continue
                    else:
                        print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                        xp -= 30
                        wolf -= 1
                elif fire > 0 and (hero_position == fire_position or hero_position == fire_position_1):
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
            if hero_position in map3:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")

                elif wolf > 0 and (hero_position == wolf_position or hero_position == wolf_position_1):
                    print("\nWOLF!!!!!!\n")
                    wolf_and_fire2()
                    f_or_r = input("Do you fight or you run: ")
                    if f_or_r == "1":
                        print("\nBy running you have saved some xp, but the wolf"
                              " is still in the island.")
                        run_count += 1
                        if run_count == 3:
                            print("\nWATCH behind you, The WOLF!!!")
                            print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                            xp -= 30
                            wolf -= 1
                        else:
                            continue
                    else:
                        print("\nWOW! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                        xp -= 30
                        wolf -= 1
                elif fire > 0 and (hero_position == fire_position or hero_position == fire_position_1):
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
            if hero_position in map3:
                if treasures > 0 and (hero_position == treasure_1 or hero_position == treasure_2):
                    xp += 20
                    treasures -= 1
                    print("\nWOW! you just found a TREASURE!!! and you got +20 xp.\n")
                elif wolf > 0 and (hero_position == wolf_position or hero_position == wolf_position_1):
                    print("\nWOLF!!!\n")
                    wolf_and_fire2()
                    f_or_r = input("Do you fight or you run: ")
                    if f_or_r == "1":
                        print("\nBy running you have saved some xp, but the wolf"
                              " is still in the island.")
                        run_count += 1
                        if run_count == 3:
                            print("\nWATCH behind you, The WOLF!!!")
                            print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                            xp -= 30
                            wolf -= 1
                        else:
                            continue
                    else:
                        print("\nWow! you have killed the Wolf, but you were injured and lost 30 xp.\n")
                        xp -= 30
                        wolf -= 1
                elif fire > 0 and (hero_position == fire_position or hero_position == fire_position_1):
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

    print("\n****-- Congratulations you have completed Level 3. --****")


bonus()
