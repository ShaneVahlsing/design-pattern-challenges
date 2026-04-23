# Create a 'CoffeeBuilder' with methods like 'add_sugar()', 'set_milk(type)', 
# and 'add_shot()'. Each method must 'return self' to allow method chaining.

from enum import Enum

class MilkType(Enum):
  OAT = 0
  WHOLE = 1
  TWO_PERCENT = 2
  ALMOND = 3

class CoffeeType(Enum):
  LATTE = 0
  MOCHA = 1
  FLAT_WHITE = 2
  DRIP = 3
  
class CoffeeBuilder:
  def __init__(coffeeType: CoffeeType):
    self.coffeeType = coffeeType
    self.sugars: int = 0
    self.milkType: MilkType = MilkType.WHOLE
    self.shots: int = 2

  def addShot(self, n: int):
    self.shots += n
    return self

  def addSugar(self, n: int):
    self.sugars += n
    return self

  def setMilkType(self, t: MilkType):
    self.milkType = t
    return self


