#teknik linear/sequential search

# def seqSearch(data, key):
#     i = 0
#     pos = i + 1
#     while(i < len (data)):
#         if data[i] == key:
#             break
#         i += 1
#         pos = i + 1
#     if pos <= len (data):
#         print("data", key, " ditemukan di posisi", pos)
#     else:
#         print("data tidak ditemukan")
#     return pos
# data = [10, 4, 9, 1, 15, 7]
# seqSearch(data, 15)

# #Teknik straitmaxmin
# def STRAITMAXMIN(A, n):
#     max = A[0]
#     min = A[0]
#     for i in range (1, n):
#         if A[i] > max:
#             max = A[i ]
#         else:
#             if A[i] < min:
#                 min = A[i]
#     print("Max =", max, ", Min =", min)

x = [22, 5, 9, 15, 21, 8, 55, 10]

bilangan = int(input("Masukan bilangan yang dicari: "))
hasil = False
for i in range (0, len(x)):
    if bilangan == x[i]:
        hasil = True
        break

if hasil:
    print ("Bilaangan: ", bilangan, "ditemukan")
else: 
    print ("Bilangan: ",bilangan, "tidak ditemukan")
