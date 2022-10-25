# Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

#function that allows for inpuut

def greet_with_name(name):
    print(f"Hell {name}")
    print(f"How do you do {name}")

greet_with_name("Angela")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hell {name}")
    print(f"What is it like in {location}")

greet_with("Froilan", "Artesia")

#Functions with keyword arguments
greet_with(location = "London", name = "Angela")