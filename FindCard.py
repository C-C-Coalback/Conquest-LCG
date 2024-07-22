import OrksCardsInit

orks_card_array = OrksCardsInit.orks_cards_init()


def find_card(card_to_find):
    i = 0
    while orks_card_array[i].get_shields() != -1:
        if card_to_find == orks_card_array[i].get_name():
            print("Card found! :", orks_card_array[i].get_name())
            return orks_card_array[i]
        else:
            i = i + 1
    retry = input("Card not found. Retry? (y/n)")
    if retry == "y":
        card_name = input("Enter card name: ")
        return find_card(card_name)
    else:
        return orks_card_array[i]


def check_card_type(card_object, required_type):
    if card_object.get_card_type() == required_type:
        return True
    else:
        return False

