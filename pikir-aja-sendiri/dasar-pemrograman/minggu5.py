#LOOPING
#program unk menemukan jumlah blgn dalam satu list
# numbers = [7, 5, 9, 8, 9, 0, 8, 4, 0]
# sum = 0
# #iterasi
# for each in numbers:
#     sum = sum + each

# print("Jumlah semuanya:", sum)

#fungsi range
'''fungsi range dapat di gunakan untuk menghasilkan deret bilangan'''
# print(range(10)) #cmn nampilin 0 - 10
# print(list(range(10))) #kalo ini jadi d list gtu
# print(list(range(2,8)))
# print(list(range(2, 20, 3))) #2 (itu angka pertamanya), 20(angka maksimal nya), 3 (mau di tambah 3, sampai ke angka maksimal nya)

#Program untuk iterasi list menggunakan pengindeksan
# mapel = ['Matematika', 'Fisika', 'Kimia']

# #iterasi list menggunakan indeks
# for i in range(len(mapel)):
#     print("Saya suka", mapel[i])

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
# ulang = 3
# for i in range (ulang):
#     print ("data ke - " + str (i + 1))
#     nama = input("masukkan nim anda : ")
#     uts = int(input("Masukkan nilai uts anda: "))
#     uas = int(input("Masukkan nilai UAS : "))
#     print ("NIM anda adalah %s nilai UTS anda adalah %i nilai UTS anda %i " % (nama, uts, uas))
#     print ("-" * 40)

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

# barang = {
#     "Buku" : {"nama" : "buku", "harga": 5000},  
#     "Pulpen" : {"nama" : "pulpen", "harga": 5000}, 
#     "Pensil" : {"nama" : "pensil", "harga": 7000},
# }

# banyakJenis = int(input("Banyak jenis : "))
# for i in range (banyakJenis):
#     print ('data ke -' + str (i + 1))
#     kode = input("Kode [Buku/Pulpen/Pensil] : ").lower()
#     if kode in barang:
#         jumlah = int(input("Banyak Barang: "))
#         hargaSatuan = barang [kode]["harga"]
#         subtotal = hargaSatuan * jumlah

# Program Kasir Sederhana
# Menggunakan konsep looping (for, while, break, continue)

# print("=" * 45)
# print("       SELAMAT DATANG DI INDOMART")
# print("=" * 45)

# # Daftar produk
# produk = {
#     "buku": 20000,
#     "pulpen": 10000,
#     "pensil": 18000,
#     "spidol": 15000,
#     "penghapus": 5000
# }

# # Tampilkan daftar produk
# print("Daftar Produk:")
# for nama, harga in produk.items():
#     print(f"- {nama.capitalize():<10}: Rp {harga:,.2f}")
# print("=" * 45)

# # Variabel utama
# daftar_belanja = []
# total = 0


# # Input awal: berapa jenis produk yang ingin dibeli
# banyak_jenis = int(input("Banyak jenis produk yang ingin dibeli: "))

# # Fungsi untuk input produk
# def input_produk(nomor, total):
#     kode = input("Masukkan nama produk: ").lower()
#     if kode in produk:
#         harga = produk[kode]
#         print(f"Harga satuan {kode.capitalize()} = Rp {harga:,.2f}")
#         jumlah = int(input("Masukkan jumlah barang: "))
#         subtotal = harga * jumlah
#         total += subtotal
#         daftar_belanja.append(f"{kode.capitalize()} x{jumlah} = Rp {subtotal:,.2f}")
#         print(f"Subtotal: Rp {subtotal:,.2f}")
#         print(f"Total sementara: Rp {total:,.2f}")
#     else:
#         print("⚠️ Produk tidak ditemukan! Coba lagi.")
        
#     return total

# # Loop awal sebanyak banyak_jenis
# for i in range(banyak_jenis):
#     print(f"\nJenis ke-{i + 1}")
#     total = input_produk(i + 1, total)

# # Tanya apakah mau menambah produk lagi
# while True:
#     tambah = input("\nApakah ingin menambah produk lain? (y/t): ").lower()
#     if tambah == "y":
#         print(f"\nJenis tambahan ke-{+ 1}")
#         total = input_produk( 1, total)
        
#     else:
#         break

# # STRUK PEMBELIAN
# print("\n" + "=" * 45)
# print("              STRUK PEMBELIAN")
# print("=" * 45)
# for i, item in enumerate(daftar_belanja, start=1):
#     print(f"{i}. {item}")
# print("-" * 45)
# print(f"Total Belanja: Rp {total:,.2f}")
# print("=" * 45)

# # PROSES PEMBAYARAN
# while True:
#     bayar = int(input("Masukkan jumlah uang pembayaran: Rp "))
#     if bayar < total:
#         kurang = total - bayar
#         print(f"⚠️ Uang Anda kurang Rp {kurang:,.2f}. Silakan bayar lagi.")
#     else:
#         kembalian = bayar - total
#         print("\nPembayaran berhasil ✅")
#         print(f"Total dibayar : Rp {bayar:,.2f}")
#         print(f"Kembalian     : Rp {kembalian:,.2f}")
#         break

# print("=" * 45)
# print("Terima kasih sudah berbelanja di Indomart 😊")
# print("=" * 45)

print("=" * 45)
print("       SELAMAT DATANG DI INDOMART")
print("=" * 45)

# Daftar produk
produk = {
    "buku": 20000,
    "pulpen": 10000,
    "pensil": 18000,
    "spidol": 15000,
    "penghapus": 5000
}

# Tampilkan daftar produk
print("Daftar Produk:")
for nama, harga in produk.items():
    print(f"- {nama.capitalize():<10}: Rp {harga:,.2f}")
print("=" * 45)

# Variabel utama
total = 0
nomor = 1

# Input awal: berapa jenis produk yang ingin dibeli
banyak_jenis = int(input("Banyak jenis produk yang ingin dibeli: "))

# Loop awal sebanyak banyak_jenis
for i in range(banyak_jenis):
    print(f"\nJenis ke-{i + 1}")
    kode = input("Masukkan nama produk: ").lower()
    if kode in produk:
        harga = produk[kode]
        print(f"Harga satuan {kode.capitalize()} = Rp {harga:,.2f}")
        jumlah = int(input("Masukkan jumlah barang: "))
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nomor}. {kode.capitalize()} x{jumlah} = Rp {subtotal:,.2f}")
        print(f"Total sementara: Rp {total:,.2f}")
        nomor += 1
    else:
        print("⚠️ Produk tidak ditemukan! Coba lagi.")

# Tanya apakah mau menambah produk lagi
while True:
    tambah = input("\nApakah ingin menambah produk lain? (y/t): ").lower()
    if tambah == "y":
        print(f"\nJenis tambahan ke-{nomor}")
        kode = input("Masukkan nama produk: ").lower()
        if kode in produk:
            harga = produk[kode]
            print(f"Harga satuan {kode.capitalize()} = Rp {harga:,.2f}")
            jumlah = int(input("Masukkan jumlah barang: "))
            subtotal = harga * jumlah
            total += subtotal
            print(f"{nomor}. {kode.capitalize()} x{jumlah} = Rp {subtotal:,.2f}")
            print(f"Total sementara: Rp {total:,.2f}")
            nomor += 1
        else:
            print("⚠️ Produk tidak ditemukan! Coba lagi.")
    else:
        break

# STRUK PEMBELIAN AKHIR
print("\n" + "=" * 45)
print("              STRUK PEMBELIAN")
print("=" * 45)
print(f"Total Belanja: Rp {total:,.2f}")
print("=" * 45)

# PROSES PEMBAYARAN
while True:
    bayar = int(input("Masukkan jumlah uang pembayaran: Rp "))
    if bayar < total:
        kurang = total - bayar
        print(f"⚠️ Uang Anda kurang Rp {kurang:,.2f}. Silakan bayar lagi.")
    else:
        kembalian = bayar - total
        print("\nPembayaran berhasil ✅")
        print(f"Total dibayar : Rp {bayar:,.2f}")
        print(f"Kembalian     : Rp {kembalian:,.2f}")
        break

print("=" * 45)
print("Terima kasih sudah berbelanja di Indomart 😊")
print("=" * 45)




        