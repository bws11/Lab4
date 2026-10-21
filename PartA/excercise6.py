count = 0
for i in range(2000, 3000):
    
    if i % 13 == 0:
        count += 1
        if count == 2:
            print(i)
            break
