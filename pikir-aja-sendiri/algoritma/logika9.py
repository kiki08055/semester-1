# # x = ['python', 'c++', 2018, 2020]
# # y = [1, 2, 3, 4, 5, 6, 7]
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
print ("ARRAY 1 DIMENSI")
X = ['Python', 'C++', 2018, 2020]
Y = [1, 2, 3, 4, 5, 6, 7]

print("Elemen pertama X:", X[0])
print("Elemen terakhir X:", X[-1])
print("Tiga elemen awal Y:", Y[:3])
print("Elemen Y index 2 sampai 5:", Y[2:6])

print("==================================================")

# Data kamu dalam bentuk 2D tapi gaya baru (tidak mirip temanmu)
print("ARRAY 2 DIMENSI")
X = [
    ['Python', 2018],
    ['C++', 2020]
]

Y = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# Akses elemen tertentu
print("X[0][0] =", X[0][0])    # Python
print("X[1][1] =", X[1][1])    # 2020

print("Y baris kedua =", Y[1])  
print("Y kolom pertama =", [Y[i][0] for i in range(len(Y))])

# Slicing baris dan kolom
print("X baris pertama =", X[0][:])
print("Y kolom kedua =", [Y[i][1] for i in range(len(Y))])
