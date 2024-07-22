import OrksCardsInit
import FindCard

orks_card_array = OrksCardsInit.orks_cards_init()
faction_wheel = ["Astra Militarum", "Space Marines", "Tau", "Eldar",
                 "Dark Eldar", "Chaos", "Orks", "Astra Militarum", "Space Marines"]


def write_deck_into_file(deck_string):
    file = open("deck_storage.txt", "a")
    file.write(deck_string)
    file.write("\n")
    file.close()


def create_deck():
    warlord_to_find = input("Enter a Warlord: ")
    # Check if Warlord exists/is Warlord
    warlord_card = FindCard.find_card(warlord_to_find)
    while not FindCard.check_card_type(warlord_card, "Warlord"):
        if FindCard.check_card_type(warlord_card, ""):
            print("Card not found.")
        else:
            print("Card is not a Warlord, card is a(n)", warlord_card.get_card_type(), "card")
        warlord_to_find = input("Enter a Warlord: ")
        warlord_card = FindCard.find_card(warlord_to_find)
    print("Card is a Warlord!")
    deck_to_write = input("Enter a name for the deck: ")
    if warlord_card.get_name() == "Nazdreg":
        deck_to_write += "#Nazdreg"
        deck_to_write += "#Nazdreg's Flash Gitz"
        deck_to_write += "#Nazdreg's Flash Gitz"
        deck_to_write += "#Nazdreg's Flash Gitz"
        deck_to_write += "#Nazdreg's Flash Gitz"
        deck_to_write += "#Kraktoof Hall"
        deck_to_write += "#Bigga is Betta"
        deck_to_write += "#Bigga is Betta"
        deck_to_write += "#Cybork Body"
        print(deck_to_write)
    required_faction = "Orks"
    cards_added_array = []
    deck_size = 8
    while deck_size < 13:  # set to 50 in a real case
        card_to_add = input("Enter a card: ")
        card_object = FindCard.find_card(card_to_add)
        if FindCard.check_faction(card_object, required_faction):
            if FindCard.check_loyalty(card_object, "Signature"):
                print("Card is a signature card, may not be added.")
            else:
                already_added = False
                for cards_added in cards_added_array:
                    if cards_added == card_object.get_name():
                        already_added = True
                if already_added:
                    print("At least one copy of this card has already been added.")
                else:
                    copies_to_add = int(input("Enter how many copies you want to add: "))
                    if copies_to_add > 3:
                        print("Can only add a maximum of 3 copies of a card to a deck.")
                    elif copies_to_add < 0:
                        print("Invalid number entered.")
                    elif copies_to_add == 0:
                        print("Card not added.")
                    else:
                        print("Adding", copies_to_add, "copies of", card_object.get_name())
                        while copies_to_add != 0:
                            deck_to_write += "#"
                            deck_to_write += card_object.get_name()
                            deck_size = deck_size + 1
                            copies_to_add = copies_to_add - 1
                        cards_added_array.append(card_object.get_name())
    write_deck_into_file(deck_to_write)
