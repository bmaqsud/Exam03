class Flyer:
    def fly(self):
        print("O'rdak ucha oladi")
class Swimmer:
    def swim(self):
        print("O'rdak suza oladi")
class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()