# Keeps track of user and their scores
class User:
  # in case we are loading user from a data source (with 
  # some already defined score)
  def __init__(self, name, score):
    self.name = name
    self.score = score

  # TODO: does this work in python ? constructor overloading ?
  def __init__(self, name):
    User(name, 0)

  def increseScore(self, amount):
    self.score += amount

  def decreaseScore(self, amount):
    self.score -= amount