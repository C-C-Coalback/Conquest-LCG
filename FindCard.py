from Inits import OrksCardsInit

orks_card_array = OrksCardsInit.orks_cards_init()


def find_card(card_to_find):
    i = 0
    while orks_card_array[i].get_shields() != -1:
        if card_to_find == orks_card_array[i].get_name():
            # print("Card found! :", orks_card_array[i].get_name())
            return orks_card_array[i]
        else:
            i = i + 1
    return orks_card_array[i]


def check_card_type(card_object, required_type):
    if card_object.get_card_type() == required_type:
        return True
    else:
        return False


def check_loyalty(card_object, required_loyalty):
    if card_object.get_loyalty() == required_loyalty:
        return True
    else:
        return False


def check_faction(card_object, required_faction):
    if card_object.get_faction() == required_faction:
        return True
    else:
        return False
