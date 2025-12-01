def selectionSort(val):
    for i in range(len(val)-1,0,-1):
        max = 0
        for l in range (1, i+1):
            if val[l]>val[max]:
                max = l
            temp = val[i]
            val[i] = val[max]
            val[max] = temp

angka = [22, 10, 15, 3, 8, 2]
selectionSort(angka)
print(angka)


def bubbleShort(x):
    for i in range (len(x)-1, 0,-1):
        max = 0
        for l in range(1, i+1):
            if x[l] > x[max]:
                max = l
        temp = x[i]
        x[i] = x[max]
        x[max] = temp

hasil = [22, 10, 15, 3, 8, 2]
bubbleShort(hasil)
print(hasil)

# def insertionSort(val):
#     for index in range(1, len(val)):
#         a = val[index] # perbandingan
#         b = index # pergeseran
#         while b > 0 and val[b - 1] > a:
#             val[b] = val [b - 1]
#             b = b - 1
#         val[b] = a

# angka = [22, 10, 15, 3, 8, 2]
# insertionSort(angka)
# print(angka)