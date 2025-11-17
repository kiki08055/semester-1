# import numpy as np

# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a)

#array dimensi 1 
# nilai_tugas = [70,80,90,"Keterangan lulus"]
# print("Nilai Tugas: \n", nilai_tugas)
'''CONTOH GPT'''
# nilai_tugas = [80, 90, 75, 88, 95, 70]
# print("Data nilai tugas:", nilai_tugas)
# print("Nilai pertama :", nilai_tugas[0])
# print("Nilai pertama :", nilai_tugas[1])
# print("Nilai pertama :", nilai_tugas[5])

# nilai_tugas[2] = 100 #mengubah isi array
# print("Nilai setelah diubah:", nilai_tugas)

#MENGISI ARRAY DENGAN INPUT
# nilai_tugas = []
# for i in range(6):
#     nilai = int(input(f"Masukkan nilai tugas ke-{i+1}: "))
#     nilai_tugas.append(nilai)

# # print("Nilai tugas yang dimasukkan: ", nilai_tugas)
# rata_rata = sum(nilai_tugas) / len(nilai_tugas)
# print("Rata-rata nilai:", rata_rata)

#DIMENSI DUA
'''disebut juga nested array
nama_array[jumlah_elemen_baris][jumlah_elemen_kolom]'''

# array = [["Teknik", "Kedokteran", "MIPA"], [1,2,3]]
# print(array)

#ARRAY DIMENSI 2 LANJUTAN
#deklarasi matriks 4 * 4
matriks =([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])

#isi matriks 4 * 4
for i in range(4):
    for j in range(4):
        if i == j:
            matriks[i][i] = 1
        if i < j:
            matriks[i][j] = 1
        if i > j: 
            matriks[i][j] = 0
for i in range(4):
    print(matriks[i])

#STUDI KASUS
# matriks =([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
# for i in range(4):
#     for j in range(4):
#         if i == j:
#             matriks[i][i] = i + 1
#         elif i > j:
#             matriks[i][j] = 0
#         else:
#             i > j
#             matriks[i][j] = j + 1
# for i in range(4):
#     print(matriks[i])
