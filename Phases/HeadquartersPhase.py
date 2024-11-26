def hq_phase(round_number, p_one, p_two):
    print("hq:", round_number)
    p_one.ready_all_in_play()
    p_two.ready_all_in_play()
    p_one.add_resources(4)
    p_two.add_resources(4)
    p_one.draw_card()
    p_one.draw_card()
    p_two.draw_card()
    p_two.draw_card()
    print(p_one.get_resources())
    print(p_two.get_resources())

def pygame_hq_phase(round_number, p_one, p_two, game_screen):
    print("hq:", round_number)
    p_one.set_phase("Headquarters")
    p_two.set_phase("Headquarters")
    p_one.ready_all_in_play()
    p_two.ready_all_in_play()
    p_one.add_resources(4)
    p_two.add_resources(4)
    p_one.draw_card()
    p_one.draw_card()
    p_two.draw_card()
    p_two.draw_card()
    p_one.toggle_initiative()
    p_two.toggle_initiative()
    print(p_one.get_resources())
    print(p_two.get_resources())
    p_one.increment_round_number()
    p_two.increment_round_number()
    if round_number < 3:
        p_one.toggle_planet_in_play(round_number + 4)
        p_two.toggle_planet_in_play(round_number + 4)
