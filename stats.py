def word_count (path):

  with open(path) as file:

    text = file.read()

  text = text.split()

  count = 0

  for word in text:
       
     count += 1

  return count

def dic_characters (path):

  dictionary = {}

  with open(path) as file:

    text = file.read()

  for character in text:

    character = character.lower()
       
    if character in dictionary:
      
      dictionary[character] += 1

    else:

      dictionary[character] = 1

  return dictionary

def sort_on (dict):
  return dict["amount"]

def sort_dict (dict):

  sorted = []

  for letter in dict.keys():

    sorted.append({"letter": letter, "amount": dict[letter]})

  sorted.sort(reverse=True, key=sort_on)

  return sorted
