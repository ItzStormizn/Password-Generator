import random

lenght=random.randint(8, 10)

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_characters = '!@#$%^&*()-+'
all = capital_letters + small_letters + numbers + special_characters

temp=random.sample(all, lenght)

password="".join(temp)

print("Generated password: " + password)