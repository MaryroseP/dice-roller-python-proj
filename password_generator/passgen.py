import string
import random

# list of characters

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)

# Take password length

user_input = int(input("How long will the password be?: "))

while True:
    try:
        char_num = int(user_input)
        if char_num < 8:
            print("Password should be more than 8 characters long to be considered strong")
            user_input = input("Enter number of charactrs for the password again: ")
            
        else:
            break
    
    except:
        print("Enter numbers only.")
        user_input = input("Enter number of charactrs for the password again: ")
        
# shuffle the contents of the list of characters

random.shuffle(lowercase)
random.shuffle(uppercase)
random.shuffle(digits)
random.shuffle(punctuation)

# compute the number of characters for letters and digits and punctuation

letter_chars = round(char_num * (30/100))
numpunc = round(char_num * (20/100))
 
 # store the resulting password in a list
result = []

 # select characters for the password. No need to use random module since the list is shuffled beforehand
 
for char in range(letter_chars):
    result.append(uppercase[char])
    result.append(lowercase[char])
    
for char in range(numpunc):
    result.append(digits[char])
    result.append(punctuation[char])
    
# randomize the position of the characters in the result

random.shuffle(result)

# join the result
password = "".join(result)
print(f"Strong password: {password}")

# Coded by Maryrose Pergis
# Reference: https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/




    
 
 
 
 
 
 
 





