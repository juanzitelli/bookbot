def get_num_words(text):
  words_count = len(text.split())
  return words_count

def get_char_count_dict(text):
  counter = {}
  sentence = text.split()
  for word in sentence:
    characters = list(word)
    for char in characters:
      lower_char = char.lower()
      if lower_char in counter:
        counter[lower_char] += 1
      else:
        counter[lower_char] = 1
  return counter

def sort_on(dic):
    return dic["num"]

def get_sorted_characters_dict(dictionary):
  formatted_dict_list = []
  for key in dictionary:
    if(key != None and key.isalpha()):
      formatted_dict_list.append({"char": key, "num": dictionary[key]})
  formatted_dict_list.sort(key=sort_on, reverse=True)
  return formatted_dict_list


def print_pretty(sorted_list):
  for item in sorted_list:
    print(f"{item['char']}: {item['num']}")