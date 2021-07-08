lo = 1
hi = 1000

print("Please think of a number between {} and {}".format(lo, hi))
input("Press ENTER to start")

guess = 1
while True:
  guess = lo + (hi - lo) // 2
  high_low = input("My guess is {}. Should I guess higher or lower? "
                   "Enter h or l, or c if my guess was correct"
                   .format(guess)).casefold()

  if high_low == "h":
    # Guess higher. Low end of the range becomes 1 greater than the guess.
    print()
  elif high_low == "l":
    # Guess lower. High end of the range becomes one less than the guess.
    print()
  elif high_low == "c":
    print("I got it in {} guesses!".format(guess))