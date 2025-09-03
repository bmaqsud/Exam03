class Student:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

    def get_ism(self):
        return self.ism

    def get_yosh(self):
        return self.yosh

    def get_kurs(self):
        return self.kurs

    def introduce(self):
        print(f"{self.ism},{self.yosh}, {self.kurs}")

s = Student("Ali", 20, 2)
s.introduce()
