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

def decoder(message, offset):
    translated_message = ''
    lower_case_message = message.lower()
    integer_offset = int(offset)
    for letter in lower_case_message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + integer_offset) % 26]
        else:
            translated_message += letter
    return translated_message

def encoder(message, offset):
    encoded_message = ''
    lower_case_message = message.lower()
    for letter in lower_case_message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            encoded_message += alphabet[(letter_value - int(offset)) % 26]
        else:
            encoded_message += letter
    return encoded_message

def encoder_path():
    message_to_encode = input('Type the message you would like to encode. > ')
    key_to_encode = input('What would you like the key to be? (type a number) > ')
    new_encoded_message = encoder(message_to_encode, key_to_encode)
    print('Here is your encoded message:')
    print(new_encoded_message)
    restart_choice = input('Would you like to encode/decode another message? Type "y" for yes and "n" for no. > ')
    if restart_choice == 'y' or restart_choice == 'Y':
        start_sequence()
    else:
        print('Goodbye.')

def decoder_path():
    message_to_decode = input('Type the message you would like to decode. > ')
    key_to_decode = input('What is the key to decode the message? (type a number) > ')
    new_decoded_message = decoder(message_to_decode, key_to_decode)
    print('Here is your decoded message:')
    print(new_decoded_message)
    restart_choice = input('Would you like to encode/decode another message? Type "y" for yes and "n" for no. > ')
    if restart_choice == 'y' or restart_choice == 'Y':
        start_sequence()
    else:
        print('Goodbye.')


#start the program
print('Welcome to the Ceasar Cipher machine.')
start_sequence()
