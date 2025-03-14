# Your Student ID:230543002
# Your Name and Surname:Osman Tat
n = int(input("Enter a number: "))
for i in range(1, n * 2, 2):
    print(" " * ((n * 2 - 1 - i) // 2) + "*" * i)

