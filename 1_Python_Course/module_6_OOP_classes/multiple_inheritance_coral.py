class Coral :

    def community(self) :
        print("Coral lives in a community.")


class Anemone :

    def protect_clownfish(self) :
        print("The anemone is protecting the clownfish.")


# we call both classes into the inheritance tuple. This means that CoralReef is inheriting
# from two parent classes.
class CoralReef(Coral, Anemone) :
    pass


# Let's instantiate a CoralReef object
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()