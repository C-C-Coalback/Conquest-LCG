# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses

# Planet cards

plannum = CardClasses.PlanetCard("Plannum",
                                 "Battle Ability: Move a non-warlord unit you control to a planet of your choice.",
                                 1, 1, False, True, True)
atrox_prime = CardClasses.PlanetCard("Atrox Prime", "Battle Ability: Deal 1 damage "
                                                    "to each enemy unit at a target HQ or adjacent planet.",
                                     1, 1, True, True, False)
barlus = CardClasses.PlanetCard("Barlus", "Battle Ability: Discard 1 card at random from your opponent's hand.",
                                2, 0, False, False, True)
elouith = CardClasses.PlanetCard("Elouith", "Battle Ability: Search the top 3 cards of your deck for a card. "
                                            "Add it to your hand, and place the remaining cards "
                                            "on the bottom of your deck in any order.", 2, 0, False, True, False)
carnath = CardClasses.PlanetCard("Carnath", "Battle Ability: Trigger the Battle ability of another planet in play",
                                 1, 1, True, True, False)
tarrus = CardClasses.PlanetCard("Tarrus", "Battle Ability: If you control fewer units than your opponent, "
                                          "gain 3 resources or draw 3 cards.", 1, 1, True, False, True)
osus_iv = CardClasses.PlanetCard("Osus IV", "Battle Ability: "
                                            "Take 1 resource from your opponent.", 0, 2, False, False, True)
ferrin = CardClasses.PlanetCard("Ferrin", "Battle Ability: Rout a target non-warlord unit.", 0, 2, True, False, False)
yvarn = CardClasses.PlanetCard("Y'varn", "Battle Ability: Each player puts a unit into play from his hand at his HQ.",
                               0, 1, True, True, True)
iridial = CardClasses.PlanetCard("Iridial", "Battle Ability: Remove all damage from a target unit.",
                                 1, 0, True, True, True)

# Orks core cards


nazdreg = CardClasses.WarlordCard("Nazdreg",
                                  "Each other unit you control at this planet gains Brutal. ",
                                  "Warrior. Warboss.", "Orks", 2, 7, 2, 5, "Bloodied.")
nazdreg_flash_gitz = CardClasses.ArmyCard("Nazdreg's Flash Gitz", "Combat Action: Deal this unit 1 damage to ready it. "
                                                                  "(Limit once per phase.)",
                                          "Nob. Warrior.", 3, "Orks", "Signature", 2, 4, 1, False)
kraktoof_hall = CardClasses.SupportCard("Kraktoof Hall", "Combat Action: Exhaust this support to move 1 damage from a "
                                                         "target unit you control to another target unit "
                                                         "at the same planet.", "Location.", 2, "Orks", "Signature",
                                        False)
bigga_is_betta = CardClasses.EventCard("Bigga is Betta", "Interrupt: When you deploy an Orks unit, "
                                                         "reduce its cost by 2. "
                                                         "Deal 1 damage to that unit after it enters play.", "Tactic.",
                                       0, "Orks", "Signature", 1, False)
cybork_body = CardClasses.AttachmentCard("Cybork Body", "Attach to an army unit.\nDouble attached unit's HP.",
                                         "Wargear. Bionics.", 1, "Orks", "Signature", 3, False)
sniveling_grot = CardClasses.ArmyCard("Sniveling Grot", "", "Runt. Ally.", 0, "Orks", "Common", 1, 1, 0, False)
goff_nob = CardClasses.ArmyCard("Goff Nob", "", "Warrior. Nob. Elite.", 5, "Orks", "Loyal", 6, 6, 0, False)
weirdboy_maniak = CardClasses.ArmyCard("Weirdboy Maniak", "Reaction: After this unit enters play, "
                                                          "deal 1 damage to each other unit at this planet.",
                                       "Oddboy. Psyker.", 3, "Orks", "Loyal", 2, 4, 1, False)
tankbusta_bommaz = CardClasses.ArmyCard("Tankbusta Bommaz", "This unit deals double damage to enemy Vehicle units.",
                                        "Warrior. Boyz.", 4, "Orks", "Common", 3, 4, 2, False)
rugged_killa_kans = CardClasses.ArmyCard("Rugged Killa Kans", "No Wargear Attachments.\nBrutal.", "Vehicle. Walker.",
                                         4, "Orks", "Loyal", 2, 5, 2, False)
enraged_ork = CardClasses.ArmyCard("Enraged Ork", "Brutal.", "Warrior. Boyz.", 2, "Orks", "Loyal", 0, 5, 1,
                                   False)
crushface = CardClasses.ArmyCard("Crushface", "Interrupt: When you deploy another Orks unit at this planet, "
                                              "reduce its cost by 1.", "Warrior. Nob.", 3, "Orks", "Loyal",
                                 2, 3, 2, True)
bad_dok = CardClasses.ArmyCard("Bad Dok", "This unit gains 3 command icons while it is damaged.", "Oddboy. Nob.", 2,
                               "Orks", "Common", 1, 4, 1, False)
rokkit_boy = CardClasses.ArmyCard("Rokkit Boy", "Each enemy unit at this planet loses the Flying keyword.",
                                  "Warrior. Boyz.", 2, "Orks", "Common", 2, 2, 1, False)
goff_boyz = CardClasses.ArmyCard("Goff Boyz", "This unit gets +3 ATK while it is at the first planet.",
                                 "Warrior. Boyz. Ally.", 1, "Orks", "Common", 0, 2, 0, False)
shoota_mob = CardClasses.ArmyCard("Shoota Mob", "", "Warrior. Boyz.", 1, "Orks", "Common", 2, 1, 1, False)
burna_boyz = CardClasses.ArmyCard("Burna Boyz", "Reaction: After this unit declares an attack against an enemy unit, "
                                                "deal 1 damage to a different enemy unit at the same planet.",
                                  "Warrior. Boyz.", 4, "Orks", "Common", 5, 3, 1, False)
battle_cry = CardClasses.EventCard("Battle Cry", "Play only during a battle.\nCombat Action: "
                                                 "Each unit you control gets +2 ATK until the end of the battle.",
                                   "Power.", 3, "Orks", "Loyal", 2, False)
snotling_attack = CardClasses.EventCard("Snotling Attack", "Deploy Action: Put 4 Snotlings tokens "
                                                           "into play divided among any number of planets.", "Tactic.",
                                        2, "Orks", "Common", 1, False)
squig_bombin = CardClasses.EventCard("Squig Bombin'", "Action: Destroy a target support card.", "Tactic.",
                                     2, "Orks", "Common", 1, False)
rokkit_launcha = CardClasses.AttachmentCard("Rokkit Launcha", "Attach to an army unit.Attached unit gains Ranged.",
                                            "Wargear. Weapon.", 1, "Orks", "Common", 1, False)
ork_kannon = CardClasses.SupportCard("Ork Kannon", "Combat Action: Exhaust this support to target a planet. "
                                                   "Each player deals 1 indirect damage among the units he controls at "
                                                   "that planet.", "Artillery. Weapon.", 1, "Orks", "Common", False)
bigtoof_banna = CardClasses.SupportCard("Bigtoof Banna", "Limited.\nInterrupt: When you deploy an Orks unit, "
                                                         "exhaust this support to reduce that unit's cost by 1.",
                                        "Upgrade.", 1, "Orks", "Common", True)
tellyporta_pad = CardClasses.SupportCard("Tellyporta Pad", "Combat Action: Exhaust this support to move an Orks unit "
                                                           "you control to the first planet.",
                                         "Location.", 2, "Orks", "Common", False)
snotling = CardClasses.TokenCard("Snotling", "", "Runt.", "Orks", 1, 1)

print(ferrin.get_red())
