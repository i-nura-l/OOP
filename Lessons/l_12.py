from l_11 import Person
if  __name__ == "__main__":

  p1 = Person("John", 'Dan', 36)
  p1.walk(); p1.info()
  p2 = Person("Mary", 'James', gender = 'male')
  p2.walk(); p2.info()
  print()

  persons = []
  persons.append(p1)
  persons.append(p2)

  for person in persons:
    print(person.info())