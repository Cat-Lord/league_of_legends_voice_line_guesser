from numpy import diff


class Game:
  def __init__(self, championAudioDict):
      self.championAudioDics = championAudioDict

  def generate_question(self, numberOfOptions):
    options = []
    for i in enumerate(numberOfOptions):
      # generate option that is not in options already
      pass