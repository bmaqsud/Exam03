class Author:
    def __init__(self,full_name):
        self.full_name=full_name
        
    def get_full_name(self):
        return self.full_name
    
class Book(Author):
    def __init__(self, book):
        self.book=book
    
    def get_book(self):
        return self.book

    def get_info(self):
        print(f"{self.full_name}, {self.book} ")

a=Author("Alisher Navoiy")
b=Book("Xamsa", a)
b.get_info()