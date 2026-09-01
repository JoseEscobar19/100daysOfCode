print("Welcome, Alice!")
print("Your score is 95")
print("---")
print("Welcome, Bob!")
print("Your score is 87")
print("---")
print("Welcome, Carol!")
print("Your score is 91")
print("---")

def greet(name):
    print("Hello", name + "!")

flavor = "mint chip"

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)

from my_module import greet, flavor

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)

