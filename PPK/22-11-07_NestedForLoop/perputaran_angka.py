n = int(input())
li = list(range(1, n))
for x in range(n-1):
    for x in li:
        print(x, end="")
    print()
    temp = li[0]	# Meng-assign li[0] pada sebuah variabel
    li.pop(0)		# kemudian menghapus li[0]
    li.append(temp)	# dan memasukkan variabel tersebut ke ujung list