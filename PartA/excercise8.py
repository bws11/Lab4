user_number = int(input("Enter a positive integer: "))
total = 1
for i in range(1, user_number + 1):
    total *= i
print(total)