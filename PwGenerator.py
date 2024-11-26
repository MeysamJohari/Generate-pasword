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
listOfCaracters = string.ascii_letters + string.digits + \
    string.punctuation  # define a variable for list of caracters
pasword = ''.join(random.sample(listOfCaracters, int(  # make a list of caracters with random sample and get a number from uset to detemine the length of password
    input("Enter the length of password: "))))
print(pasword)
