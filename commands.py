class Command:
  def __init__(self, target, action, amount, item) -> None:  
    self.target = target
    self.action = action
    self.amount = amount
    self.item = item
  
  def toJson(self):
    command = {
      "target": self.target,
      "action": self.action
    }
    
    if self.amount:
      command["amount"] = self.amount
    if self.item:
      command["item"] = self.item

    return command


class Target:
  MINIONS = "minions"
  GAME = "game"
  VOLUME = "volume"

class Soldier:
  WARRIOR = "warrior"
  RIDER = "rider"
  RANGED = "ranged"

class Action:
  BUY = "buy"
