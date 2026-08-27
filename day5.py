#battle game
#task 1: setup game variables and thier stats

# character var
wizzard = "Wizzard"
elf = "Elf"
human = "Human"

# hitpoint hp of each character
wizzard_hp = 70
elf_hp = 100
human_hp = 150

# damage points of each char
wizzard_damage = 150
elf_damage = 100
human_damage = 20

#dragon hp and damage points
dragon_hp = 300
dragon_damage = 50

#task2: prompt player to choose from list of otpions
#task3: setup infinite loop to handle player choice

while True:
    print("1) Wizzard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character:")

    if character == "1":
        character = wizzard
        my_hp = wizzard_hp
        my_damage = wizzard_damage
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("unknown character")
        break

print("you have choosen" + character);
print("Health:" + str(my_hp))
print("Damage:" + str(my_damage))


'''
i was misunderstanding, its not pulling from the print info, 
that is just to informt he user, once they choose a number, 
then i input manualy the rest of the info in the code
'''

#task4: battle a dragon and simulate loosing points 
