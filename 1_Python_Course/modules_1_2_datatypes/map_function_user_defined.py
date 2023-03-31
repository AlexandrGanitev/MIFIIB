aquarium_creatures = [
    {"name" : "sammy", "species" : "shark", "tank number" : 11, "type" : "fish"},
    {"name" : "ashley", "species" : "crab", "tank number" : 25, "type" : "shellfish"},
    {"name" : "jo", "species" : "guppy", "tank number" : 18, "type" : "fish"},
    {"name" : "jackie", "species" : "lobster", "tank number" : 21, "type" : "shellfish"},
    {"name" : "charlie", "species" : "clownfish", "tank number" : 12, "type" : "fish"},
    {"name" : "olly", "species" : "green turtle", "tank number" : 34, "type" : "turtle"}
]


# We’ve decided that all the aquarium creatures are in fact going to move into the same tank.
# We need to update our records to reflect that all of our creatures are moving into tank 42.
# To have map() access each dictionary and each key:value pair in the dictionaries, we construct
# a nested function:

def assign_to_tank(aquarium_creatures: object, new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number
        return x

    return map(apply, aquarium_creatures)


"""
We define an assign_to_tank() function that takes aquarium_creatures and new_tank_number as parameters. 
In assign_to_tank() we pass apply() as the function to map() on the final line. The assign_to_tank 
function will return the iterator resulting from map().

apply() takes x as an argument, which represents an item in our list — a single dictionary.

Next we define that x is the "tank number" key from aquarium_creatures and that it should store 
the passed in new_tank_number. We return each item after applying the new tank number.

We call assign_to_tank() with our list of dictionaries and the new tank number we want to 
replace for each creature:"""

assigned_tanks = assign_to_tank(aquarium_creatures, 42)
print(list(assigned_tanks))
print('*' * 25, "Пример 2")
base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]
# Next we pass in pow() as our function into map() and provide the two lists as our iterables:

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)
print('*' * 25, "Пример 3")
base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)
# As a result, nothing will change within the calculation of this program and so it will still
# yield the same result:

# Output
# [2, 16, 216, 4096, 100000]