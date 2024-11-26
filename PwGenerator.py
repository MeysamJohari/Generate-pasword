import random
import string


def generate():  # define a function
    length = random.randint(16, 20)  # define a variable for length of password
    password = ''.join(random.choice(string.ascii_letters + string.digits)
                       for i in range(length))  # define a variable for password
    return password


print(generate())  # call the function
