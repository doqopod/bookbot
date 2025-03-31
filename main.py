import sys

def get_book_text (path):
  
  with open(path) as file:

    text = file.read()

    return text
  
def main ():

  if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  else:
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print ("----------- Word Count ----------")
    words = word_count(sys.argv[1])
    print(f"Found {words} total words")
    print ("--------- Character Count -------")
    sorted = sort_dict (dic_characters(sys.argv[1]))
    for item in sorted:
     print (f"{item["letter"]}: {item["amount"]}") 

from stats import word_count

from stats import dic_characters

from stats import sort_dict

main()