from name import Book
if  __name__ == "__main__":

  b1 = Book("Demon Slayer", 'Nothing', price='700c')
  b2 = Book('Punpun', 'Inoasano', 'PI2091')
  b3 = Book("1984", 'George Orwell', 'GO-243', '1000c')
  b1.search(); b1.info();  b2.search(); b2.info(); b3.search(); b3.info()
  print()
