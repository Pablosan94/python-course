lo = 1
hi = 1000

print("Please think of a number between {} and {}".format(lo, hi))
input("Press ENTER to start\n")

guesses = 1
while lo != hi:
  guess = lo + (hi - lo) // 2
  hi_lo = input("My guess is {}. Should I guess higher or lower? "
                   "Enter h or l, or c if my guess was correct\n"
                   .format(guess)).casefold()

  if hi_lo == "h":
    # Guess higher. Low end of the range becomes 1 greater than the guess.
    lo = guess + 1
  elif hi_lo == "l":
    # Guess lower. High end of the range becomes one less than the guess.
    hi = guess - 1
  elif hi_lo == "c":
    print("I got it in {} guesses!".format(guesses))
    break
  else:
    print("Please enter h, l or c")

  guesses += 1
else:
  print("You thought of the number {}".format(lo))
  print("I got it in {} guesses!".format(guesses))