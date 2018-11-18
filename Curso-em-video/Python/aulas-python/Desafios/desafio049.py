t = int(input("Digite qual tabuada você quer: "))
n = 0
for c in range(0, 11):
    print("{} * {} = {}".format(t, n, t * n))
    n += 1