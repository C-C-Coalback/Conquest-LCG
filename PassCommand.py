def check_for_pass(x, y, player_number):
    print(x, y, player_number)
    if player_number == 1:
        if 1100 < x < 1150 and 600 < y < 650:
            print("player one pass")
            return 1
    else:
        if 50 < x < 100 and 50 < y < 100:
            print("player two pass")
            return 1
    return 0