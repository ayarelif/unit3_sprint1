from pdb import set_trace as breakpoint
from random import randint, sample
import unittest

class Product():
    def __init__(self,identifier, name, price=None, weight=None,flammability=None):
        self.name=name
        def_num1=10
        self.price=price if price is not None else def_num1
        def_num2=20
        self.weight=weight if weight is not None else def_num2 
        def_num3=0.5   
        self.flammability=flammability if flammability is not None else def_num3
        self.identifier=randint(1000000, 9999999)

    def stealability(self):
        stealability=self.price/self.weight
        if stealability < 0.5:
          return "Not so stealable..."
        elif 0.5< stealability <1.0:
          return "Kinda stealable."
        else:
          return "Very stealable"

    def explode(self):
        product=self.flammability*self.weight
        if product <10:
          return "...fizzle."
        elif 10<= product < 50:
          return "...boom!"
        else: 
          return "...BABOOM!"

class BoxingGlove(Product):
  # designates the class should inherit from the product class
    def __init__(self,identifier, name, price=None, weight=None, flammability=None):
      def_num4=10
      self.weight=weight if weight is not None else def_num4  
      super().__init__(self,identifier,name)
    def explode(self):
      return "... it's a glove"
    def punch(self):
      if self.weight<5:
        return "That tickles."
      elif 5<= self.weight <15:
        return "Hey that hurt!"
      else:
        return "OUCH!"




if __name__=="__main__":
  
  #part1
    prod = Product("A Cool Toy",25,45,1)
    print(prod.name)
    print(prod.price)
    print(prod.flammability)
    print(prod.weight)
    print(prod.identifier)


  #part2
    print(prod.stealability())
    print(prod.explode())
    

  #part3

    glove = BoxingGlove('Punchy the Third',"Elif")
    print(glove.price)
    print(glove.weight)
    print(glove.punch())
    print(glove.explode())


   
   