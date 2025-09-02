def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def main():
  path_to_file = "Bookbot/books/frankenstein.txt"
  book_text = get_book_text(path_to_file)
  num_words = count_words(book_text)
  print(f"{num_words} words found in the document")
main()

