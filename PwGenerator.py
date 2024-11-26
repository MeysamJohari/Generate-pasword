import random
import string

# #First way
# def generate():  # define a function
#     length = random.randint(16, 20)  # define a variable for length of password
#     password = ''.join(random.choice(string.ascii_letters + string.digits)
#                        for i in range(length))  # define a variable for password
#     return password


# print(generate())  # call the function
 # Second way
listOfCaracters = string.ascii_letters + string.digits +string.punctuation
pasword = ''.join(random.sample(listOfCaracters, 24))
print(listOfCaracters)