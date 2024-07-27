def find_deck():
    file_to_read = open("deck_storage.txt", "r")
    deck_name = input("Enter deck name: ")
    deck_found = False
    file_text = file_to_read.read()
    pos = 0
    current_deck = ""
    while not deck_found and pos < len(file_text):
        while file_text[pos] != "#":
            current_deck += file_text[pos]
            pos += 1
        if current_deck == deck_name:
            print("Deck found")
            deck_found = True
        else:
            while file_text[pos] != "\n":
                pos += 1
            pos += 1
    file_to_read.close()
    if not deck_found:
        print("Deck not found")
        return ""
    return current_deck
