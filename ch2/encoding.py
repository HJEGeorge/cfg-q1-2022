def encode_character(char):
    return 'axz5' + char + '3jqs'

def cipher():

    pw = input("Enter secret password")

    if pw != "password":
        raise ValueError("STAY AWAY")

    word = input("Please enter a word you want to encode: ")

    encoded_word = ""

    for char in word:
        encoded_word += encode_character(char)

    return encoded_word

print(cipher())