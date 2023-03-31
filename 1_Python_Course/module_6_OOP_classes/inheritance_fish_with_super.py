# https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
class Fish :
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False) :
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self) :
        print("The fish is swimming")

    def swim_backwards(self) -> classmethod :
        print("The fish can swim backwards")


class Trout(Fish) :
    def __init__(self, water="freshwater") :
        self.water = water
        super().__init__(self)
        # Можно super() заменить такой конструкцией:
        # Fish.__init__(self, first_name="Terry")
        # terry.first_name = "Terry"


terry = Trout()
# Initialize first name
terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)
# Use child __init__ override
print(terry.water)
# Use parent swim() method
terry.swim()


class Clownfish(Fish) :
    def live_with_anemone(self) :
        print("The clownfish in coexisting with sea anemone.")


casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()


# We have overridden the initialized parameters in the __init__() method, so that the last_name variable
# is now set equal to the string "Shark", the skeleton variable is now set equal to the string "cartilage",
# and the eyelids variable is now set to the Boolean value True. Each instance of the class can also override
# these parameters.
class Shark(Fish) :
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True) :
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self) :
        print("The shark cannot swim backwards, but it can sink backwards.")


sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
