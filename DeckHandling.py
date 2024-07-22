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
    write_deck_into_file(deck_to_write)
