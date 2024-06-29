alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount  # Use modulo to handle shifts beyond the length of the alphabet
            end_text += alphabet[new_position]
        else:
             end_text += clear

    print(f"The {cipher_direction}d is {end_text}")



should_continue = True
while should_continue:
     
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift % 26
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you wanna go again. Otherwise type 'no'.\n")
    if result == "no":
         should_continue = False
         print("Good Bye")




