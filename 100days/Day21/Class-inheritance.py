class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish:
    def swim(self):
        print("moving in water")

class Fish2(Animal):
    def __init__(self):
        super().__init__()       

    def swim(self):
        print("-----\nmoving in water")
    
    def breathe(self):
        super().breathe()
        print("Doing this underwater")

nemo = Fish()
nemo.swim()

nemo2 = Fish2()
nemo2.swim()
nemo2.breathe()
print(f"nemo2 has {nemo2.num_eyes} eyes.")
