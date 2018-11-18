from time import sleep
import emoji
n = 10
for c in range(0,11):
    print(n)
    n -= 1
    sleep(1)
    if n == 0:
        print(emoji.emojize(":boom: :boom: AAAAEEEEEEEE :boom: :boom:"))
