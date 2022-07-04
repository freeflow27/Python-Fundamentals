def print_upper_words(words):
    """Print each word on a new line, and uppercase them"""
    for word in words:
        print(word.upper)


def print_upper_words2(words):
    """print words on new lines, uppercased, but ony if the start with e/E"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """print word on new lines, uppercase them, and only if the ystart with the given letter"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})