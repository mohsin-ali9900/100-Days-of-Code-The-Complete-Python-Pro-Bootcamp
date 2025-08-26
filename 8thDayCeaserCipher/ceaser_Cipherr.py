alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encode_decode_function(Input_Text,shift,EnORDe):
        result = "" 
        if EnORDe == "decode":
            shift = shift*(-1)
        
        for letter in Input_Text:
            if letter in alphabet:
                positionOfLetter = alphabet.index(letter)
                new_Position = (positionOfLetter + shift) % 26
                result = result + alphabet[new_Position]
            else:
                result = result + letter
        return result

again = "yes"    
while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    final_result = encode_decode_function(text,shift,direction)
    print(f"Here is the  reult: {final_result}")    
    again = input("Type 'yes' if you want to go again. Otherwise say 'no' :")