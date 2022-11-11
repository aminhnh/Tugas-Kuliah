n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+i), end="") # Fungsi chr() mengubah angka menjadi sebuah karakter sesuai ASCII
    print()