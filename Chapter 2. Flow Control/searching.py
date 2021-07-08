shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

if item_to_find in shopping_list:
  found_at = shopping_list.index(item_to_find)

if found_at:
  print("Item found at position {}".format(found_at))
else:
  print("{} not found".format(item_to_find))