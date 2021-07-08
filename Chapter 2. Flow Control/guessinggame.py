import random

highest = 10
maxTries = 10
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
guesses = 0

while guess != answer and guesses < maxTries:
  guess = int(input())

  if guess == 0:
    print("Bye bye")
    break

  if guess == answer:
    print('You win')
    break
  else:
    if guess < answer:
      print('My number is a bit higher')
    else:
      print('My number is a bit lower')

  guesses += 1

if guesses >= 10:
  print("\nYou had {} tries!".format(maxTries))