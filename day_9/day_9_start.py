# Dictionary
# Left - Key
# Right - Value

programming_dictionary = {"Bug": "An error in a program that prevents thr program from running as expected.",
"Function" : "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to a dictionary
programming_dictionary["Loop"] = "The action of doing somethig over and over again"
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
'''programming_dictionary = {}
print(programming_dictionary)'''

# Edit an item in a dictionary
programming_dictionary["Bug"] = "a moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])


# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin", 
}

# Nesting a List in a Dictionary

travel_log = [
    {
        "country" : "France" , 
        "cities_vistied" : ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12
        },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin", "Hamberg", "Stuggart"], 
        "total" : 5
        },
]