class Car :
    def __init__(self,brand,model,year ):
        self.brand=brand
        self.model=model
        self.year=year


    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_info(self):
        print(f"{self.brand},{self.model}, {self.year}")


car = Car("BMW", "X5", 2020)
car.get_info()