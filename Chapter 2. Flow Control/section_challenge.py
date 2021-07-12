def print_menu(menu_items):
  print("Please choose your option from the list below:")

  for item in menu_items:
    item_index = menu_items.index(item) + 1
    print("{}.\t{}".format(item_index, item))
  
  print("0.\tExit")

menu_items = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
selection = -1

while selection != 0:
  print_menu(menu_items)
  selection = int(input())

  if selection != 0 and selection <= len(menu_items):
    print("You selected {}".format(menu_items[int(selection - 1)]))
  elif selection > len(menu_items):
    pass
  else:
    break