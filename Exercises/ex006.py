# Your Student ID:230543002
# Your Name and Surname:Osman Tat
numbers = list(range(1, 11))
print("Original list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)
numbers.extend([11, 12, 13])
print("Extended list:", numbers)
print("List length:", len(numbers))
numbers.pop(0)
numbers.pop(-1)
print("Modified list:", numbers)
even_numbers = sorted([num for num in numbers if num % 2 == 0])
print("Sorted even numbers:", even_numbers)
