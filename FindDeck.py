def find_deck():
    file_to_read = open("deck_storage.txt", "r")
    deck_name = input("Enter deck name: ")
    file_text = file_to_read.read()
    pos = 0
    current_deck = ""
    while pos < len(file_text):
        while file_text[pos] != "#":
            current_deck += file_text[pos]
            pos += 1
        if current_deck == deck_name:
            print("Deck found")
            file_to_read.close()
            return read_deck(pos)
        else:
            while file_text[pos] != "\n":
                pos += 1
            pos += 1
            current_deck = ""
    file_to_read.close()
    print("Deck not found")
    return ""


def read_deck(pos):
    file_to_read = open("deck_storage.txt", "r")
    deck_contents = ""
    file_text = file_to_read.read()
    while file_text[pos] != "\n":
        deck_contents += file_text[pos]
        pos += 1
    return deck_contents
