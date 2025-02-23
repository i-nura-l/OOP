
class Mathutil:

   @staticmethod
   def is_even(n):
       return n%2==0

   @staticmethod
   def is_prime(n):
       if n < 2:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True
'''

class Mathutil:

   pi = 3.1415

   @staticmethod
   def sum(a,b):
       return a+b

   @staticmethod
   def div(a,b):
       return a/b

   @staticmethod
   def is_even(n):
       return n%2==0

   @staticmethod
   def is_prime(n):
       if n < 2:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True
'''