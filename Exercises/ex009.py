# Your Student ID:230543002
# Your Name and Surname:Osman Tat
choice = input("Convert (C to F) or (F to C)? Enter C or F: ").upper()
temp = float(input("Enter temperature: "))
if choice == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is {converted:.2f}°F")
elif choice == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is {converted:.2f}°C")
else:
    print("Invalid choice!")
