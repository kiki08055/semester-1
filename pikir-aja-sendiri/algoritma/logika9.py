x = ['python', 'c++', 2018, 2020]
y = [1, 2, 3, 4, 5, 6, 7]
# # print (x[0]: , x[0])
# # print (y[2:4]: , y[2:4])

# # List awalj
# x = ['python', 'c++', 2018, 2020]
# y = [1, 2, 3, 4, 5, 6, 7]

# # Akses elemen tunggal
# print("Elemen pertama dari x  :", x[0])
# print("Elemen ketiga dari x   :", x[2])

# # Slicing list
# print("Elemen y dari index 2 sampai 3 :", y[2:4])

# # Panjang list
# print("Panjang list x :", len(x))
# print("Panjang list y :", len(y))

# # Print semua elemen x dengan looping
# print("Isi list x:")
# for i in range(len(x)):
#     print(f"  x[{i}] = {x[i]}")

# # Print semua elemen y dengan looping
# print("Isi list y:")
# for j in range(len(y)):
#     print(f"  y[{j}] = {y[j]}")


# Array 1 Dimensi
# print ("ARRAY 1 DIMENSI")
# X = ['Python', 'C++', 2018, 2020]
# Y = [1, 2, 3, 4, 5, 6, 7]

# print("Elemen pertama X:", X[0])
# print("Elemen terakhir X:", X[-1])
# print("Tiga elemen awal Y:", Y[:3])
# print("Elemen Y index 2 sampai 5:", Y[2:6])

# print("==================================================")

# array 2 dimensi
# print("ARRAY 2 DIMENSI")
# X2 = [
#     ['Python', 2018],
#     ['C++', 2020],
# ]

# Y2 = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]

# akses elemen tertentu
print("X[1][1] =", x[0])    # 1 pertama utk ngambil baris index kedua, 0 ke dua utk ngambil kolom index kedua
print("X[0][1] =", y[2:4])    # ini sama kayak yang atas, baris ke satu, kolom ke 2

# print("Y baris kedua =", Y2[2])  # buat ngambil baris index ke 2 (coba coba aja)
# print("Y kolom pertama =", [Y2[i][0] for i in range(len(Y2))]) #looping nya buat ambil angka dari array yg beda

# # slicing baris dan kolom
# print("X baris pertama =", Y2[0][:]) # [:] untuk ngambil semua elemen kolom d baris itu
# print("Y kolom kedua =", [Y2[i][1] for i in range(len(Y2))])
