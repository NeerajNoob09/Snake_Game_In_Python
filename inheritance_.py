class Animal:
    def __init__(self):
        self.no_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.no_of_eyes)
