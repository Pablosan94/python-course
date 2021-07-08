# Imports the os.path standard library to use the function splitext.
import os.path

def preprocess(path):
  # List of tuples that we are going to fill from the file.
  tuples = []
  # Flag to skip the first line.
  first_line = True
  # We will store the headers here.
  first_line_text = ''

  # We open the file at the given path.
  file = open(path)

  # Traverse all lines in the file.
  for line in file:
    # Conditional to process the first line (headers).
    if first_line:
      # Store the headers text.
      first_line_text = line
      # Set the flag to false to avoid coming here again.
      first_line = False
      # Skip to the next iteration of the loop.
      continue

    # Splits the values in every line
    line_split = line.split('\t')
    # Add a tuple of type (index, value) converting both to floating point numbers.
    tuples.append( (float(line_split[0]), float(line_split[1].rstrip())) )
  # END LOOP

  # We create another list of tuples where but this one is sorted using the sorted function.
  sorted_tuples = sorted(tuples, key=lambda t: t[0])
  
  return sorted_tuples

# Takes in the sorted tuples and the value to search for.
def split_at_index(sorted_tuples, split_index):
  # If the value is in the first column of the tuples list, stores it inside result.
  result = [index for index, tup in enumerate(sorted_tuples) if tup[0] == split_index]
  # If result is not an empty list, it means the value has been found, so it is returned. 
  if result:
    return result[0]
  # In case the value is not found, the function is called again trying with the previous value + 1. 
  else:
    return split_at_index(sorted_tuples, split_index + 1)

# Takes in the sorted tuples and the index previously obtained by calling split_at_index().
def list_from_tuples(sorted_tuples, index):
  # Definition of the variables to be stored.
  lower_list = []
  upper_list = []
  lists = []

  # Loop to populate the lower_list.
  for tuple in sorted_tuples[:index]:
    lower_list.append(tuple)

  # Loop to populate the upper_list.   
  for tuple in sorted_tuples[index:]:
    upper_list.append(tuple)

  # Generate the list containing both lower_list and upper_list.
  lists.append(lower_list)
  lists.append(upper_list)
  
  # Return the list of lists.
  return lists

# EXAMPLE OF EXECUTION ORDER
# tuples = preprocess('data.txt')
# index = split_at_index(tuples, 35)
# lower_list = list_from_tuples(tuples, index)[0]
# upper_list = list_from_tuples(tuples, index)[1]