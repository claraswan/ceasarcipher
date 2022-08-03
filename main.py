alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuation = ".,?'!:();$@#%*+=- "

def start_sequence():
    choice = input('Would you like to encode or decode a message? Type "e" for encode and "d" for decode. > ')
    if choice == 'e' or choice == 'E':
        encoder_path()
    elif choice == 'd' or choice == 'D':
        decoder_path()
    else:
        print("I didn't understand your choice. Please try again.")
        start_sequence()
