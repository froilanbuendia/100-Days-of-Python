import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
valid = True
print(art.logo)

def caesar(text, shift, direction):
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if direction == "encode":
        cipher = ''
        for i in range(len(text)):
            if text[i] in alphabet:
                cipher += alphabet[(alphabet.index(text[i]) + shift ) % 26]
            else:
                cipher += text[i]
        print(f"the encrypted text is {cipher}")
    elif direction == "decode":
        decrypted = ''
        for i in range(len(text)):
            if text[i] in alphabet:
                decrypted += alphabet[(alphabet.index(text[i]) - shift) % 26]
            else:
                decrypted += text[i]
        print(f"The decoded text is {decrypted}")


while valid:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Import and print the logo from art.py when the program starts.
    #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 



    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    caesar(text, shift, direction)
    user = input("Would you like to play again? y/n").lower()
    if user == 'n':
        print("Goodbye!")
        valid = False