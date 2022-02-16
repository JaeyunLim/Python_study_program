sum = 0
for i in range(1,1001):
    if i % 2 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        sum += i
print(sum % 1004)