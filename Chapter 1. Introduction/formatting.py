for i in range(1, 13):
  print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

#
# To define the number of spaces for a parameter to take, you can use :X where X is the number of spaces.
# For alignment, :<X gives left-alignment whilst :>X gives right-aligment. 
# Additionally, :^X exists for center-alignment.
#
for i in range(1, 13):
  print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

for i in range(1, 13):
  print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
