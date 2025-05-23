def is_alphabet(ch):
 if len(ch) != 1:
  return False
 return ch.isalpha()
character = input("Enter a character: ")
if is_alphabet(character):
    print(f"'{character}' is an alphabet.")
else:
    print(f"'{character}' is not an alphabet.")