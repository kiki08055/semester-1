# #LOOPING
# #program unk menemukan jumlah blgn dalam satu list
# numbers = [7, 5, 9, 8, 9, 0, 8, 4, 0]
# sum = 0
# #iterasi
# for each in numbers:
#     sum = sum + each

# print("Jumlah semuanya:", sum)

# #fungsi range
# '''fungsi range dapat di gunakan untuk menghasilkan deret bilangan'''
# print(range(10)) #cmn nampilin 0 - 10
# print(list(range(10))) #kalo ini jadi d list gtu
# print(list(range(2,8)))
# print(list(range(2, 20, 3))) #2 (itu angka pertamanya), 20(angka maksimal nya), 3 (mau di tambah 3, sampai ke angka maksimal nya)

# #Program untuk iterasi list menggunakan pengindeksan
mapel = ['Matematika', 'Fisika', 'Kimia']

#iterasi list menggunakan indeks
for i in range(len(mapel)):
    print("Saya suka", mapel[i])

#WHILE

# count = 0
# while (count < 5):
#     print("The c ount is:", count)
#     count = count + 1
# print("Good bye!")

#infinite loop
'''kondisi loop selelu benar dan tidak pernah salah
di sebut loop tidak terbatas'''

# count = 0
# while (count < 5):
#     print("The count is:", count)
#     count = count
# print("Good bye!")

#kendali looping ( akan berhenti klo kondisi udh false)
#contoh menggunakan statment break
# for letter in "pythonProgramming":
#     if letter == "g":
#         break
#     print("Huruf sekarang:", letter)
# print("Good bye")

#pake continue "g" nya di abaikan
# for letter in "pythonProgramming":
#     if letter == "g":
#         continue
#     print("Huruf sekarang:", letter)
# print("Good bye")

# #WHILE ELSE
# count = 0
# while (count < 8):
#     print(count, "kurang dari 8")
#     count = count + 1
# else:
#     print (count, "tidak kurang dari 8")

#LATIHAN 
ulang = 3
for i in range (ulang):
    print ("data ke - ", (i + 1))
    nama = input("masukkan nim anda : ")
    uts = int(input("Masukkan nilai uts anda: "))
    uas = int(input("Masukkan nilai UAS : "))
    print ("NIM anda adalah %s nilai UTS anda adalah %i nilai UTS anda %i " % (nama, uts, uas))
    #$s (nama yg berupa string), kalo %i (ini buat int) sesuai type data
    print ("-" * 40)

#GEROBAK FRIED CHICKEN
#ketentuan:
'''- setiap pembeli dikenakan pajak sebesar 10%
- banyak jenis, jenis potong dan banyak beli diinput'''

# print ("\nGEROBAK FRIED CHICKEN")
# print ("------------------------")
# print ("\nKode JenisPotong Harga")
# print ("------------------------")

# menu = {
#     "D" : {"nama" : "dada", "harga" : 2500},
#     "P" : {"nama" : "Paha", "harga" : 2000},
#     "S" : {"nama" : "Sayap", "harga" : 1500}
# }

# for kode, info in menu.items():
#     print(f"{kode} - {info['nama']:<10} Rp. {info['harga']}")

# print ("-" * 40)

# #input yng d beli berapa banyak
# banyak_jenis = int(input("Banyak jenis: "))

# #list untuk menyimpan data pembelian 
# pembelian = []
# totalHarga = 0

# #input jenis
# for i in range(banyak_jenis):
#     print(f"\nJenis ke-{i+1}")
#     kode = input("Kode Potong [D/P/S] : ").upper()
#     if kode in menu:
#         jumlah = int(input("Banyak Potong: "))
#         harga_satuan = menu[kode]["harga"]
#         subtotal = harga_satuan * jumlah
#         pembelian.append({
#             "no" : i+1,
#             "jenis": menu[kode]["nama"],
#             "harga": harga_satuan,
#             "jumlah": jumlah,
#             "subtotal": subtotal
#         })
#         totalHarga += subtotal
#     else:
#         print("kode tidak ditemukan")

# #hitung pjk + total bayar
# pajak = totalHarga * 0.1
# totalBayar = totalHarga + pajak

# print ("\n\n===================STRUK PEMBELIAN===================")
# print ("No   Jenis Potong   Harga  Jumlah  Subtotal")
# for item in pembelian:
#     print(f"{item['no']:<3} {item['jenis']:<13} Rp.{item['harga']:<6} {item["jumlah"]:<7} Rp.{item['subtotal']}")
# print ("-" * 50)
# print (f"Jumlah Bayar : Rp.{totalHarga:,.2f}")
# print (f"Pajak : Rp.{pajak:,.2f}")
# print (f"Total Bayar : Rp.{totalBayar:,.2f}")
# print ("-" * 50)


##Genap
# number = 0

# for i in range(2,101,2):
#     print(i)
#     number= number + i

# print ("\njumlah semuanya:", number)


'''subtotal, total sementara, input barang lg ga? klo ada nambah lagi jadi perulangan ke dua, subtotal ke dua sama yg ke satu
jumlah barang yg d beli berapa, masukkan pembayaran nya, terus ada kembalian kalo kurang pake else (uang ga cukup di suruh masukkin lagi)'''

