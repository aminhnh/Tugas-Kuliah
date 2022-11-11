mas = ord(input())	# Fungsi ord() mengubah string menjadi integer sesuai dengan ASCII
huruf = 65  		# 65 merupakan ASCII dari "A"
for x in range(1, 8):	# Terdapat 7 baris
    for y in range(x):
        if huruf > 90:	# 90 merupakan ASCII untuk "Z"
        	break		# Memberhentikan loop agar tidak mencetak huruf setelah "Z" dalam ASCII
        if huruf < mas:
            print(chr(mas)+" ", end="")	# Fungsi chr() mengubah angka menjadi sebuah karakter sesuai ASCII
        else:
            print(chr(huruf)+" ", end="")
        huruf += 1
    print()	# Mencetak spasi setelah setiap iterasi