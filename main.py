from stats import get_num_words, get_char_count_dict, get_sorted_characters_dict, print_pretty
from sys import argv, exit

def main ():
  if(len(argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
  path = argv[1]
  with open(path) as f:
    file_contents = f.read()
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {get_num_words(file_contents)} total words
--------- Character Count -------
""")
    print(print_pretty(get_sorted_characters_dict(get_char_count_dict(file_contents))))
    print("============= END ===============")
main()