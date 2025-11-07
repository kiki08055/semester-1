# #Branching percabangan
# #di gunakan untuk satu pilihan keputusan

# nilai = int(input("Masukkan nilai : "))
# if nilai >= 70 :
#     print ("Selamat anda lulus ujian")
# else:
#     print ("Tidak lulus ujian")

# print("=" * 40)

# #menentukan bilangan ganjil genap 
# #string lebih identik dengan text
# nilai = int(input ("Masukkan angka = "))
# if nilai % 2 == 0:
#     print (" Bilangan {} adalah genap.".format(nilai))
# else:
#     print (" Bilangan {} adalah ganjil.".format(nilai))
# print("=" * 40)

# #program if... elif ... else
# nilai = int(input ("Masukkan angka = "))
# if nilai >= 80:
#     print ("Grade = A", nilai)
# elif nilai >= 70:
#     print("Grade = B", nilai)
# elif nilai >= 40:
#     print("Grade = D", nilai)
# else :
#     print ("Grade E", nilai)

# print("=" * 40)

# #KEHAMILAN
# hamil = int(input("Masukkan minggu : "))
# if hamil <= 20:
#     print ("ancaman keguguran")
# else: 
#     print ("anu")

# print("=" * 40)

# #PROGRAM NESTED IF
# merk = input ("Merk Baju P/A/S : ")
# if merk == 'P':
#     print("Merk Polo")
#     ukuran = input("Ukuran L/M/S: ")
#     if ukuran == 'L':
#        print("Harga == 225000")
#     elif ukuran == "M":
#         print("Harga = 175000")
#     else:
#         print("Hargan= 175000")
# elif merk == "A" :
#     print ("Merk Alisan")
#     ukuran = input("Ukuran L/M/S: ")
#     if ukuran == 'L':
#        print("Harga == 275000")
#     elif ukuran == "M":
#         print("Harga = 200000")
#     else:
#         print("Hargan= 150000")
# else:
#     print("Merk StYess")
#     ukuran = input("Ukuran L/M/S")
#     if ukuran == 'L':
#        print("Harga == 250000")
#     elif ukuran == "M":
#         print("Harga = 175000")
#     else:
#         print("Hargan= 125000")

# print("=" * 40)

# #STUDI KASUS 1
# #tentukan keluaran algoritma berikut
# a = int(input("Masukkin di sini : "))
# b = int(input("Masukkin di sini : "))
# if a > b :
#     c = a * b
# else :
#     c = a + b
#     d = c * c
# print (c)
# print (d)

# #studi kasus 2
# a = int(input("masukka angka "))
# b = int(input("masukka angka "))

# if a + b < 10 :
#     c = a - b
#     print("C =", c) #pake print di sini biar kondisinya bisa ke cut
# else :
#     c = a + b
#     d = 2 * c + b
#     print ("C", c)
#     print ("D", d)

# print("=" * 40)

# #STUDI KASUSU 3
# '''3 jam sewa rp 6000/jam
# jam berikutnya 5000/jam'''

# jam = int(input("Masukkan jam : "))
# if jam <= 3 :
#     jumlah = jam * 6000
#     print (jumlah)
# else:
#     jumlah2 = jam * 5000
#     print(jumlah2)

# print("=" * 40)

# #STUDI KASUS 4
gaji_pokok = 5000000
product_terjual = int(input("Masukkan jumlah produk terjual: "))
penjualan_target = 100 
hargaPerBarang = int(input ("Masukkan harga barang : "))
jumlah = product_terjual * hargaPerBarang
print("=" * 40)

if product_terjual >= penjualan_target:
    bonus =  gaji_pokok * 0.2 
else:
    bonus =  gaji_pokok * 0.1


total = gaji_pokok + bonus

print(f"Bonus yang didapat : Rp{bonus:,.2f}")
print(f"ga tau jumlah apaan : Rp{jumlah:,.2f}")
print(f"Total gaji yang didapat : Rp{total:,.2f}")

print("=" * 40)

#STUDI KASUS 5
# nama = input("Masukkan nama: ")
# gajiPokok = 3000000
# pajak = gajiPokok * 0.1
# tunjangan = gajiPokok * 0.2
# total_jam = int(input("Masukkan berapa jam kamu kerja: "))

# if total_jam > 200:
#     jam_lebih = total_jam - 200
#     bonus = jam_lebih * 20000
# else:
#     bonus = 0

# # total gaji
# total_gaji = gajiPokok + tunjangan + bonus - pajak

# print(f"\nNama: {nama}")
# print(f"Gaji Pokok: Rp{gajiPokok:,}")
# print(f"Tunjangan: Rp{tunjangan:,}")
# print(f"Pajak: Rp{pajak:,}")
# print(f"Bonus (jika ada): Rp{bonus:,}")
# print(f"Total Gaji Diterima: Rp{total_gaji:,}")
