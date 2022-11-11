# 2022-11-08

# Menerima Input
x,y = [int(i) for i in input().split()]
xx,yy = [int(i) for i in input().split()]
# x, y, xx, yy = 5, 5, 0, 0

# Membuat matriks
peta = [["*"]*x for i in range(y)]
n = 1
peta[0][0] = "0"
x1, y1 = xx, yy  #x1 dan y1 merupakan variable yang akan diiterasi

# Mengedit matriks
if xx!=0 and yy!=0:
    for i in range(-1, len(peta)-1):
        if x1>x-1 or y1>y-1: 
        	break
        peta[y1][x1] = str(n)
        x1, y1 = x1+xx, y1+yy
        n += 1

# Print matriks peta
for i in range(len(peta)):
    print("".join(peta[i]))