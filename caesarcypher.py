from cypherlogo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text,shift_amount,cipher_direction):
    end_of_text = ""
    if cipher_direction == 'decode':
            shift_amount *= -1
    for char in start_text:
      if char in alphabet:  
        position = alphabet.index(char)
        new_position = (position + shift_amount) % 26
        new_letter = alphabet[new_position]
        end_of_text += new_letter
      else: 
          end_of_text += char
    print(f"the {cipher_direction} on solving is {end_of_text}")
caesar(text,shift,direction)
should_continue = True
while should_continue:  
    again = input("Type 'yes' if u want to play again.Otherwise type 'no: \n")
    direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)

    if again == "no":
        should_continue = False
        print("goodbye")