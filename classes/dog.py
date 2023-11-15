from mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, rested=False, is_good=True):
        super().__init__(name, rested)
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, is_good={self.is_good}, rested={self.rested})"

    def make_sound(self):
        return "Woof!"
    
    def sleep(self):
        super().sleep()
        print(f"{self.name} is rested")

    def run_around(self):
        super().run_around()
        return "ZOOMIES!"