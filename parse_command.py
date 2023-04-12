from commands import Command, Target, Soldier, Action
from word2number import w2n

buyMinionActions = {
  Action.BUY,
  "Purchase",
  "Order",
  "Spawn",
  "Auto"
}

volumeActions = {
  "Turn up",
  "Turn down",
  "Turn off",
  "Turn on"
}

gameActions = {
  "Start",
  "Pause",
  "Stop"
}

itemWarriors = {
  "worrior",
  "warrior",
  "worriors",
  "warriors",
  "melee",
  "axeman",
  "axemen",
  "X-Men",
  "Ax Men",
  "ax-men",
  "axmen",
  "ax man",
  "ax",
  "axe",
  "oxen",
  "ox",
  "oxmen",
  "oxman"
}

itemRiders = {
  "rider",
  "horseman",
  "horse",
  "bear dwarf",
  "bear"
}

itemRangeds = {
  "ranged",
  "crossbowman",
  "crossbowmen",
  "archer",
  "crossbow man"
}

def parse_command(text):

  action = get_action(text)
  target = get_target(action)
  amount = get_amount(text)
  item = get_item(text)

  if action is None or target is None:
    return None

  return Command(
    target=target,
    action=action,
    amount=amount,
    item=item
  )

def get_action(text):
  text = text.lower()

  for word in buyMinionActions:
    if word.lower() in text:
      return Action.BUY
  
  for word in volumeActions:
    if word.lower() in text:
      return word.lower()
    
  for word in gameActions:
    if word.lower() in text:
      return word.lower()

def get_target(action):
  if action == Action.BUY:
    return Target.MINIONS
  
  for word in volumeActions:
    if word.lower() == action:
      return Target.VOLUME
  
  for word in gameActions:
    if word.lower() == action:
      return Target.GAME

def get_amount(text):
  words = text.split()
  
  for word in words:
      if word.isdigit():
          return int(word)
      else:
          try:
              return w2n.word_to_num(word)
          except ValueError:
              pass

  return None

def get_item(text):
  text = text.lower()

  for word in itemWarriors:
    if word.lower() in text:
      return Soldier.WARRIOR
  
  for word in itemRiders:
    if word.lower() in text:
      return Soldier.RIDER
  
  for word in itemRangeds:
    if word.lower() in text:
      return Soldier.RANGED
  
  return None
