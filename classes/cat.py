from mammal import Mammal

class Cat(Mammal):

    def __init__(self, name, rested=False, lives_remaining=9):
        super().__init__(name, rested)
        self.lives_remaining = lives_remaining

    def __repr__(self):
        return f"Cat(name={self.name}, lives_remaining={self.lives_remaining}, rested={self.rested})"

    def make_sound(self):
        return "meow"
    
    def sleep(self):
        super().sleep()
        print("Taking a 24 hour nap")

    # def run_around(self):
    #     self.rested = True

ursula = Cat(name="Ursula")