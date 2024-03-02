##PASSWORD GENERATOR WITH PYTHON
#This program generates a random password of length 8 to 12 characters. 
import random
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+']
password = ""
length = random.randit(8,12) ##Using the randint function from the random module to generate a random number between 8 and 12
for i in range(length):
    password += random.choice(characters) ##appends the characters selected randomly by the function random.choice

print(f"Generated Password is: {password}")
print(password)