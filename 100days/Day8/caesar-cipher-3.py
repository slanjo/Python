alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
    result = ""
    
         
    if direction == "decode":
        shift *= -1

    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        result += alphabet[new_position] 

    print(f"The {direction}d text is {result}")




#if direction == "encode":
#  encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
#  decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)
