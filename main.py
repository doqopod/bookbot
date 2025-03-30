def get_book_text (path):
  
  with open(path) as file:

    text = file.read()

    return text
  
def main ():

  print ("============ BOOKBOT ============")
  print ("Analyzing book found at books/frankenstein.txt...")
  print ("----------- Word Count ----------")
  words = word_count("books/frankenstein.txt")
  print(f"{words} words found in the document")
  print ("--------- Character Count -------")
  sorted = sort_dict (dic_characters("books/frankenstein.txt"))
  for item in sorted:
    print (f"{item["letter"]}: {item["amount"]}") 

from stats import word_count

from stats import dic_characters

from stats import sort_dict

main()