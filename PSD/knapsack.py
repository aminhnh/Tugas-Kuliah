# Tugas Praktikum Struktur Data
# 29/05/23


import numpy as np

def KS(n, C):
    if arr[n][C] != None:
    # if arr[n][C] != 0:
        return arr[n][C]
    if n == 0 or C == 0:
        result = 0
    elif w[n] > C:
        result = KS(n-1, C)
    else:
        temp1 = KS(n-1, C)
        temp2 = v[n] + KS(n-1, C-w[n])
        result = max(temp1, temp2)
    arr[n][C] = result
    return result

n = 3+3+5+10+5
w = [None] + 3*[2360] + 3*[2120] + 5*[1890] + 10*[3770] + 5*[2870]
v = [None] + 3*[91] + 3*[71] + 5*[105] + 10*[103] + 5*[96]
C = 25000
arr = np.zeros((n+1, C+1))
arr = [[None for j in range(C+1)] for i in range(n+1)]

a = KS(n, C)
print(a)




# def KS(n, C):
#     if arr[n][C] != None:
#         return arr[n][C]
#     if n == 0 or C == 0:
#         result = 0
#     elif w[n] > C:
#         result = KS(n-1, C)
#     else:
#         temp1 = KS(n-1, C)
#         temp2 = v[n] + KS(n-1, C-w[n])
#         result = max(temp1, temp2)
#     arr[n][C] = result
#     return result


# n = 5
# C = 25000
# arr = np.empty((n, C), dtype=None)
# print(arr)









# def knapsack(n, kapasitas):
#     if 

# def main():
#     [["Apel", "Jeruk", "Pisang","Kiwi","Mangga"],
#      [91, 71, 105, 103, 96],
#      [2360, 2120, 1890, 3770, 2870],
#      [3, 3, 5, 10, 5]]
#     global arr = np.zeros()
#     print("A")

# if __name__=="__main__":
#     main()