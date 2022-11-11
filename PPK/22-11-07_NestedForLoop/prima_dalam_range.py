n = int(input())
import math
prima = []
for x in range(2, n+1):
    val = True
    for y in range(2, int(math.sqrt(x))+1):  #range dibatasi untuk mengecek sampai akar dari n
        if x%y == 0:
            val = False
            break
    if val: prima.append(str(x))
print(" ".join(prima))