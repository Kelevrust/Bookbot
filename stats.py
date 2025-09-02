def count_words(text):
  words = text.split()
  return len(words)


def count_characters(text):
  char_counts = {}
  for char in text:
    lowered_char = char.lower()
    if lowered_char in char_counts:
      char_counts[lowered_char] += 1
    else:
      char_counts[lowered_char] = 1
  return char_counts


def sort_on(d):
  return d["num"]


def sort_characters(char_counts_dict):
  char_list = []
  for char, count in char_counts_dict.items():
    char_list.append({"char": char, "num": count})
  
  char_list.sort(reverse=True, key=sort_on)
  return char_list
