available_parts = ["computer", "monitor", "keyboard", "mouse", "hdmi cable", "dvd drive"]
valid_choices = []
for i in range(1, len(available_parts) + 1):
  valid_choices.append(str(i))
current_choice = "-"
computer_parts = []

while current_choice != '0':
  if current_choice in valid_choices:
    print("Adding {}".format(current_choice))
    index = int(current_choice) - 1
    chosen_part = available_parts[index]
    computer_parts.append(chosen_part)
  
  else:
    print("Please add options from the list below:")
    for index, part in enumerate(available_parts):
      print("{0}: {1}".format(index + 1, part))

    print("0: to finish")
  
  current_choice = input()

print(computer_parts)