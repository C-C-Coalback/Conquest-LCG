from Inits import PlanetCardsInit


def resolve_command_struggle(planet_num, p_one, p_two):
    player_one_command = p_one.count_command_at_planet(planet_num)
    player_two_command = p_two.count_command_at_planet(planet_num)
    if player_one_command > player_two_command:
        print(player_one_command, "greater than",
              player_two_command, "at planet no", planet_num, ",", p_one.get_name_player(), "wins command")
        return 1
    elif player_two_command > player_one_command:
        print(player_two_command, "greater than",
              player_one_command, "at planet no", planet_num, ",", p_two.get_name_player(), "wins command")
        return 2
    else:
        print("command is equal")
        return 0


def command_phase(round_number, p_one, p_two):
    planet_array2 = PlanetCardsInit.planet_cards_init()
    planet_name = input("Choose a planet to send the Warlord to:")
    pos = p_one.search_planets_in_game(planet_name)
    if pos == -1:
        print("Planet not found")
    else:
        print("Attempting to move Warlord")
        p_one.commit_warlord_to_planet(pos + 1)
    p_one.print_cards_in_play()
    p_one.print_headquarters()
    planet_name = input("Choose a planet to send the Warlord to:")
    pos = p_two.search_planets_in_game(planet_name)
    if pos == -1:
        print("Planet not found")
    else:
        print("Attempting to move Warlord")
        p_two.commit_warlord_to_planet(pos + 1)
    p_two.print_cards_in_play()
    p_two.print_headquarters()
    print("command:", round_number)
    planet_num = round_number
    planets_counted = 0
    c_res = [0, 0, 0, 0]
    while planet_num < 7 and planets_counted < 5:
        result = resolve_command_struggle(planet_num, p_one, p_two)
        print("Test", result)
        if result == 1:
            planet_name = p_one.get_planet_name_given_position(planet_num - 1)
            print("Planet name:", planet_name)
            for i in range(len(planet_array2)):
                if planet_name == planet_array2[i].get_name():
                    print("Resources of", planet_name, planet_array2[i].get_resources())
                    print("Cards of", planet_name, planet_array2[i].get_cards())
                    c_res[0] += planet_array2[i].get_resources()
                    c_res[1] += planet_array2[i].get_cards()
                    print("test", c_res[0])
        elif result == 2:
            planet_name = p_two.get_planet_name_given_position(planet_num - 1)
            print("Planet name:", planet_name)
            for i in range(len(planet_array2)):
                if planet_name == planet_array2[i].get_name():
                    print("Resources of", planet_name, planet_array2[i].get_resources())
                    print("Cards of", planet_name, planet_array2[i].get_cards())
                    c_res[2] += planet_array2[i].get_resources()
                    c_res[3] += planet_array2[i].get_cards()
                    print("test", c_res[2])
        planets_counted += 1
        planet_num += 1
    print(c_res[0], c_res[1], c_res[2], c_res[3])
    print("Player one gets", c_res[0], "resources from command struggle")
    p_one.add_resources(c_res[0])
    print("Player one gets", c_res[1], "cards from command struggle")
    for i in range(c_res[1]):
        p_one.draw_card()
    print("Player two gets", c_res[2], "resources from command struggle")
    p_two.add_resources(c_res[2])
    print("Player two gets", c_res[3], "cards from command struggle")
    for i in range(c_res[3]):
        p_two.draw_card()
    # player two will need the same idea but with c_res[2] and c_res[3]
    print(p_one.get_resources())
    print(p_one.get_cards())
    print(p_two.get_resources())
    print(p_two.get_cards())
