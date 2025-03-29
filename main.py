def get_book_text (path):
  
  with open(path) as file:

    text = file.read()

    return text
  
def main ():

  words = word_count("books/frankenstein.txt")

  print(f"{words} words found in the document")

  print (dic_characters("books/frankenstein.txt"))

from stats import word_count

from stats import dic_characters

main()