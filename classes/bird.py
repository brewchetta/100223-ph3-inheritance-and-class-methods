class Bird:

    some_bird_variable = "not real"

    all_birds = []
    bird_count = 0

    def __init__(self, name):
        self.name = name
        # add the new bird to all_birds
        Bird.all_birds.append(self)
        # increment bird_count
        Bird.bird_count += 1

    def __repr__(self):
        return f"Bird(name={self.name})"

    def tweet(self):
        return f"{self.name} is posting all their tweets... I mean X's"

    @classmethod
    def make_them_all_real(cls):
        cls.some_bird_variable = "OH NO BIRDS"

    def make_them_real(self):
        self.some_bird_variable = "they're real AGGGHHHHHH"

tweety = Bird("Tweety Bird")