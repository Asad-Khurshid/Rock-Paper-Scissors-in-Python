import random

def play():
  user = input ('Enter your choice. Press "r" for rock, "p" for paper and "s" for sissors ')
  computer = random.choice(["r", "p", "s"])

  if user == computer:
    return "it's a tie."
  if who_win(user, computer):
    return "You WON!"
  
  return "You LOST :("

def who_win(player, opponent):
  if (player == "r" and opponent == "s") or (player =="s" and opponent == "p") or (player == "p" and opponent == "r"):
    return True

while True:
  print (play())
