n = 0
n2 = 0
for c in range(0, 501):
    if n % 3 == 0:
        n2 += n
    n += 1
print(n2)