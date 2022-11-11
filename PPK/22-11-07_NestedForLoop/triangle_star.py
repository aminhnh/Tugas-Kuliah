n = int(input())
if n == 1: print("*")
else:
    for i in range(1, n+1):
        for j in range(i):
            print("#", end="")
        print()