# Your Student ID:230543002
# Your Name and Surname:Osman Tat
text = input("Enter a string: ")
char_count = {char: text.count(char) for char in sorted(set(text))}
print("Character frequencies:")
for char, count in char_count.items():
    print(f"{char}: {count}"
