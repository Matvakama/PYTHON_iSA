from Day10.Game import Character, Dice

# d4 = Dice(sides=4)
d6 = Dice(sides=6)
# d8 = Dice(sides=8)
# d10 = Dice(sides=10)
# d12 = Dice(sides=12)
# d20 = Dice(sides=20)

player = Character(HP = 20, DEF = 8, DMG = 1)
enemy = Character()

for number in range(40):
    defrolld6 = d6.roll()
    if defrolld6 > 3:
        print(f"Enemy attack parried!")
    else:
        enemy.attack(player)
        print(f"Enemy dealt {enemy.DMG} damage. You have {player.DEF} armor and {player.HP} HP left.")

    if int(player.HP) <= 0:
        print(f"You died. Try again?")
        break
    else:
        pass

    atkrolld6 = d6.roll()
    if atkrolld6 < 3:
        print(f"Your attack missed!")
    else:
        player.attack(enemy)
        print(f"You dealt {player.DMG} damage.")

    if int(enemy.HP)<=0:
        print(f"Enemy has been killed! Congratulations!")
        break
    else:
        pass

# while int(enemy.HP)>0 and int(player.HP)>0:
#     defrolld6 = d6.roll()
#     if defrolld6 > 3:
#         print(f"Enemy attack parried!")
#     else:
#         enemy.attack(player)
#         print(f"Enemy dealt {enemy.DMG} damage. You have {player.DEF} armor and {player.HP} HP left.")
#
#     if int(player.HP) <= 0:
#         print(f"You died. Try again?")
#         break
#     else:
#         pass
#
#     atkrolld6 = d6.roll()
#     if atkrolld6 < 3:
#         print(f"Your attack missed!")
#     else:
#         player.attack(enemy)
#         print(f"You dealt {player.DMG} damage.")
#
#     if int(enemy.HP)<=0:
#         print(f"Enemy has been killed! Congratulations!")
#         break
#     else:
#         pass
