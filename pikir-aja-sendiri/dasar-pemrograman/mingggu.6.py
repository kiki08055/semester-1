# #LIST TUPLE
# # #list kosong
# my_list = []
# #list berisi integer 
# my_list = [1,2,3,4,5]
# #integer berisi type campuran
# my_list = [1,2.5, "hello"]
# #list bersarang/nessted
# my_list = ["hello", [2,4,6], ['a','b']]


#MENGAKSES LIST NYA 

# my_list = ['I', 'Love', 'Python', 'Programming', 2017]
# print(my_list[0])
# print(my_list[2])

# #list dalam list
# your_list = ["hello",[1,2,3], "python"]
# # print(your_list[[1][0]])
# print(your_list[1][2])

#index error
# print (my_list[6])

# #LIST DENGAN INDEKS NEGATIF
# my_list = ['p','y','t','h','o','n']
# print (my_list[-2])

# #SLICING (MEMOTONG) LIST
# my_list = ['p','y','t','h','o','n','i','n','d','o']
# # #anggota list dari 3-5 (dari h-d)
# print(my_list[3:6])
# print(my_list[4:])
# print(my_list[:5]) #dari pertama sampe ke berapa 
# print(my_list[-1:-10]) #karena jalan nya ke kanan 

# #Mengubah anggota list
# #list adalh tipe data yg bersifat mutable (bisa diubah)

# #misal ada nilai yang salah
# ganjil= [1,3,4,7,9]
# #ubah item ke 3 (indeks ke 2)
# ganjil[2] = 5
# print (ganjil)

# #mengubah sekali banyak 
# ganjil [2:5] = [11,13,15] #darimana sampai mana
# print(ganjil)

'''METODE LIST'''

# #MENAMBAHKAN ANGGOTA LIST
# '''fungsi append() untuk menambahkan anggota ke dalam list.
# metode extend() menambahkan anggota list ke dalam list'''

# ganjil = [1,3,5,7]
# ganjil.append(9)
# print(ganjil)
# ganjil.extend([11, 13, 15])
# print(ganjil)

# '''bisa menggunakan dua operator + untk menggabungkan dua list
# dan operator * untuk melipat gandakan list'''
# genap = [2, 4, 6]
# print(genap + [8, 10, 12]) #pake + minus nya ga d taro
# print(['p', 'y',] * 2)

# #Menyisipkan anghota list
# ganjil = [5, 7, 11, 13, 15]
# #kita akan menyisipkan 9 setelah 7

# ganjil.insert(2,9)
# print(ganjil)

# MENGHAPUS ANGGOTA LIST

# my_list = ['p','y','t','h','o','n']
# my_list.remove('p') #menghapus isi bukan index, terus cmn menghapus satu karakter yg sama
# print(my_list)
# my_list.remove('n')

# my_list2 = ['p','y','t','h','o','n']
# print(my_list2.pop()) #menghapus berdasarkan index, kalo buka kurung nya kosong yg d hapus belakang

# my_list3 = ['p','y','t','h','o','n']
# del my_list3[2:]
# print(my_list3)

# my_list4 = ['p','y','t','h','o','n']
# my_list4.clear()
# print(my_list4)

# #MENGURUTKAN ANGGOTA LIST
# #menyortir bisa pake sort()
# alfabet = ['a', 'b', 'd', 'f', 'e', 'c', 'h', 'g', 'j', 'i']
# alfabet.sort()
# print(alfabet)
# alfabet.sort(reverse=True) # membalikkan 
# print(alfabet)

#TUPLE 
# Tuple kosong
# my_tuple = ()
# print(my_tuple)

# # Tuple berisi satu elemen → perhatikan tanda koma di akhir!
# my_tuple = (1,)
# print(my_tuple)

# # Tuple berisi beberapa elemen
# my_tuple = (1, 2, 3)
# print(my_tuple)

# # Tuple bersarang
# my_tuple = ("hello", [1, 2, 3], (4, 5, 6))
# print(my_tuple)

# # Memasukkan anggota tuple ke variable yang bersesuaian (unpacking)
# a, b, c = my_tuple
# print(a, b, c)

#MENGAKSES ANGGOTA TUPLE
# my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')
# #akses dari index 0 - 2
# print (my_tuple[:3])
# print (my_tuple[2:6])
# print (my_tuple[3:])


#ITERASI PADA TUPLE
# nama = ('Galih', 'Kiki')
# for name in nama:
#     print('Hi', name)

#Fungsi bawaan tuple
# my_tuple = ('p','y','t','h','o','n','i','n', 'd', 'o')
# print(my_tuple.count('n'))
# print(my_tuple.index('n'))

#STUDI KASUS

# LIST & TUPLE

# Membuat list dua dimensi (list bersarang)
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0, 0, 0]
# ]

# # Menampilkan isi list dengan format sesuai permintaan
# print("Baris Pertama, Kolom Pertama Adalah :")
# print(data[0][0])

# print("Baris Pertama, Kolom Kedua Adalah :")
# print(data[0][1])

# print("Baris Pertama, Kolom Ketiga Adalah :")
# print(data[0][2])

# print("Baris Ketiga, Kolom Ketiga Adalah :")
# print(data[2][2])

# print("Baris Ke Empat, Kolom Pertama Adalah :")
# print(data[3][0])

# list_nim = []
# list_uts = []
# list_uas = []
# list_total = []

# ulang = 2
# for i in range (ulang):
#     print ("data ke -" + str(i+1))
#     list_nim.append(input("masukkin nim anda: "))
#     list_uts.append(int(input("Masukkan nilai uts anda: ")))
#     list_uas.append(int(input("masukkan nilai uas: ")))
#     #proses
# for i in range (ulang):
#     list_total.append((list_uas[i] + list_uts[i]/2))

# print("="*80)
# print("NIM       Bilai UTS     Nilai UAS    Total")
# print("="*80)
# for i in range(ulang):
#     print ("%s \t %i \t\t %i \t\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
# print("="*80)





'''TUPLE CONTOH DOSEN'''
my_tuple = ('M', 'A', 'R', 'U', 'L', 'O', 'H')
#SLICING TUPLE
print(my_tuple[1:5])
print(my_tuple[:4])
print(my_tuple [3:])

#ubah tuple(syarat is tuple harus berupa list)
my_tuple2 = (5,4,[3,3])
my_tuple2[2][1]=2
print(my_tuple2)

#penugasan kembali
my_tuple2 = ('A', 'B', 'C')
print(my_tuple2)

del my_tuple2

#Cek anggota
my_tuple3 = ('M', 'A', 'R', 'U', 'L', 'O', 'H')
print('A' in my_tuple3)
print('B' not in my_tuple3)

#ITERASI PADA TUPLE
nama = ('Galih', 'Kiki')
for name in nama:
    print('Hi', name)

#Fungsi bawaan tuple
my_tuple = ('p','y','t','h','o','n','i','n', 'd', 'o')
print(my_tuple.count('n'))
print(my_tuple.index('n'))