##step 1 - Encryption
from art import logo
print(logo)
# position = alphabet.index(text[0])
# new_position = position + shift
# print(new_position)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet 
# by the shift amount and print the encrypted text.  
# e.g. 
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

##Step 2

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
    # Then call the correct function based on that 'drection' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.

##Step 3

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
    
#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

restart = True
while restart:
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def encrypt():
        cipher_text = ''
        for i in text:      
            if shift > 26:
                new_shift = shift % 26  
                position = alphabet.index(i) + new_shift
                character = alphabet[position]
            elif i not in alphabet:
                character = i
            else:
                position = alphabet.index(i) + shift
                character = alphabet[position]
            cipher_text += character
        print(f"The encoded text is {cipher_text}")

    def decrypt():
        plain_text = ''
        for i in text:      
            if shift > 26:
                new_shift = shift % 26  
                position = alphabet.index(i) - new_shift
                character = alphabet[position]
            elif i not in alphabet:
                character = i
            else:
                position = alphabet.index(i) - shift
                character = alphabet[position]
            plain_text += character
        print(f"The decoded text is {plain_text}")

        




    def ceaser():
        if direction == 'encode':
            encrypt()
        elif direction == 'decode':
            decrypt()
        else:
            print('error')
    ceaser()

        

    if input('Do you want to restart the cipher program?\n') == 'yes':
            ceaser()
    else:
            restart = False
