class Book:  # is templete how

    # constructor - special method to initialize attributes
    def __init__(self, title, author, code=None, price=None):
        self.title = title
        self.author = author
        self.code = code
        self.price = price

    # methods
    def search(self):
        print('The title of the book:', self.title, 'The author:', self.author)

    def info(self):
        print('The ISBN:', self.code, 'The price is', self.price)