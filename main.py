# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses

card1 = CardClasses.ArmyCard("Splintered Path Acolyte",
                             "Interrupt: When you deploy a Daemon unit, sacrifice this "
                             "unit to reduce its cost by 2", "Cultist. Tzeentch.", 1, "Chaos", "Common", 1, 1, 1)
print("Name: ", card1.get_name())
print("Text: ", card1.get_text())
print("Traits: ", card1.get_traits())
print("Cost: ", card1.get_cost())
print("Faction: ", card1.get_faction())
print("Loyalty: ", card1.get_loyalty())
print("Shields: ", card1.get_shields())
print("Attack: ", card1.get_attack())
print("Health: ", card1.get_health())
print("Command: ", card1.get_command())

card2 = CardClasses.WarlordCard("Zarathur, High Sorcerer",
                                "Interrupt: When damage is assigned to "
                                "an enemy unit at this planet, "
                                "increase that damage by 1.", "Psyker. Tzeentch.", "Chaos",
                                1, 6, 1, 5,
                                "Bloodied.")

print(card2.get_name())
print(card2.get_text())
print(card2.get_traits())
print(card2.get_cost())
print(card2.get_faction())
print(card2.get_loyalty())
print(card2.get_shields())
print(card2.get_attack())
print(card2.get_health())
print(card2.get_bloodied_attack())
print(card2.get_bloodied_health())
print(card2.get_bloodied_text())
