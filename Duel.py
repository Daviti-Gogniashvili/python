import random as rd
import time

class Duel:
  weapons = ["ak-47", "AWM"]
  player_list = []

  def __init__(self, name):
    self.name = name

  def weapon(self):
    print(self.name,"shot first with",rd.choice(Duel.weapons))


  def countdown(self):

    while self > -1:
      time.sleep(1)
      print(self)
      self -= 1
      if self == -1:
        Duel.weapon(rd.choice(Duel.player_list))


shooter1 = Duel("David")
shooter2 = Duel("Droid")
Duel.player_list.append(shooter1)
Duel.player_list.append(shooter2)
Duel.countdown(3)
