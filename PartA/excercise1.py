# Print all even numbers from 1-21 with a for loop
# Print all odd numbers from 1-20 with a while loop
print("Even numbers 1-21: ", end='')
# 1-21
for i in range(1, 22): 
    # if even
    if i % 2 == 0:
        print(f"{i}, ", end='')

print("Odd numbers 1-20: ", end='')
# reset i because of previous for loop
i = 1
# 1-20
while i <= 20:
    # if odd
    if i % 2 == 1:
        print(f"{i}, ", end='')
    i += 1