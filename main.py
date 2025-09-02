import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path_to_file = sys.argv[1]
  book_text = get_book_text(path_to_file)
  num_words = count_words(book_text)
  print(f"--- Begin report of {path_to_file} ---")
  print(f"{num_words} words found in the document")
  print()

  char_counts = count_characters(book_text)
  sorted_chars = sort_characters(char_counts)
  
  for item in sorted_chars:
    char = item["char"]
    if char.isalpha():
      count = item["num"]
      print(f"{char}: {count}")
  
  print("--- End report ---")

main()
