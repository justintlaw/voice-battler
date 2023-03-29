from commands import Command, Target, Soldier, Action

def parse_command(text):
  return Command(
    target=Target.MINIONS,
    action=Action.BUY,
    amount=1,
    item=Soldier.WARRIOR
  )
