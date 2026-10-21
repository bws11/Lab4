total = 0
for i in range(1, 100):
    if i % 3 != 0 and i % 2 == 0:
        total += i

print(total)