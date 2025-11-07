# def kalkulator():
#     print("=== Kalkulator Sederhana ===")
#     print("Penjumlahan")
#     print("Pengurangan")
#     print("Perkalian")
#     print("Peembagian")

#     pilihan = input("Pilih operasi (1/2/3/4): ")

#     try:
#         angka1 = int(input("Masukkan angka pertama: "))
#         angka2 = int(input("Masukkan angka kedua: "))
        
#         if pilihan == "1":
#             hasil = angka1 + angka2
#             print(f"Hasil: {hasil}")
#         elif pilihan == "2":
#             hasil = angka1 - angka2
#             print(f"Hasil: {hasil}")
#         elif pilihan == "3":
#             hasil = angka1 * angka2
#             print(f"Hasil: {hasil}")
#         elif pilihan == "4":
#             if angka2 != 0:
#                 hasil = angka1 / angka2
#                 print(f"Hasil: {hasil}")
#             else:
#                 print("Error: Tidak bisa dibagi dengan nol!")
#         else:
#             print("Pilihan tidak valid!")
#     except ValueError:
#         print("Input harus berupa angka!")

# kalkulator()

# bill1 = 45
# bill2 = 55 
# bintang = bill1 + bill2

# print ("bill1 adalah", bill1)
# print ("bill1 adalah", bill2)
# print("Jumlah ke duanya adalah ", bintang)


#input output
# print ("=+=+=+=+ Data Diri Mahasiswa =+=+=+=+")
# nim = input("Nim : ")
# nama = input("Nama lengkap : ")
# jurusan = input("Jurusan : ")
# alamat = input("Alamat : ")

# print ("Hasil cetak data diatas adalah")
# print ("Nim :" +str(nim))
# print ("Nama :" +str(nama))
# print ("Jurusan :" +str(jurusan))
# print ("Alamat :" +str(alamat))

# Program Jual Beli Sederhana

# # Daftar produk dengan harga
# produk = {
#     "Apel": 5000,
#     "Jeruk": 7000,
#     "Mangga": 10000,
#     "Pisang": 4000
# }

# keranjang = {}

# print("=== Selamat Datang di Toko Buah ===")
# print("Daftar Produk:")

# # Tampilkan daftar produk
# for nama, harga in produk.items():
#     print(f"- {nama}: Rp{harga}")

# while True:
#     # Pilih produk
#     pilih = input("\nMasukkan nama produk yang ingin dibeli (atau ketik 'selesai'): ").capitalize()

#     if pilih == "Selesai":
#         break

#     if pilih in produk:
#         jumlah = int(input(f"Masukkan jumlah {pilih} yang ingin dibeli: "))

#         if pilih in keranjang:
#             keranjang[pilih] += jumlah
#         else:
#             keranjang[pilih] = jumlah

#         print(f"{jumlah} {pilih} ditambahkan ke keranjang.")
#     else:
#         print("Produk tidak tersedia!")

# # # Hitung total belanja
# print("\n=== Struk Belanja ===")
# total = 0
# for nama, jumlah in keranjang.items():
#     harga = produk[nama]
#     subtotal = harga * jumlah
#     total += subtotal
#     print(f"{nama} x{jumlah} = Rp{subtotal}")

# print(f"Total Belanja: Rp{total}")
# print("Terima kasih sudah berbelanja 😊")

# nilai atau substring dari string, kita menggunakan indeks dalam tanda [].
# var1 = 'Hello Python'
# var2 = 'i LOVE apa yak'
# print("var1[0]", var1[0]) 
# print("var2[2:6]:", var2[2:6])

#slice/index dari 0
# var1 = 'Hello Python Keren' 
# var2 = var1[:13]
# print(var1)
# print("String Update: - ", var2 + 'imupp')

#tanda kutip tiga/string multibaris

# kata = 'Kuliah'
# kalimat = "BSI aja"
# paragraf = """Kuliah..?
# BSI aja"""

# print (kata)
# print (kalimat)
# print (paragraf)


#string mutible
# var1 = "Hello Python"
# var2 = "Programming with python"
# print (var1)
# print (var2)

#mengakses nilai string
# var1 = 'Hello python'
# var2 = 'I love python'
# print("var1[0]", var1[5])
# print("var2[2:6]", var2[2:6])

#mengupdate string
# var1 = 'Hello python'
# var2 = var1[:6]
# # print(var1)
# print('String update: - ', var1[:6] + 'world')

#menggabungkan string
# str1 = 'Hello'
# str2 = 'Python'

# #menggunakan + 
# print('str1 + str2 =', str1 + str2)
# #menggunakan *
# print('str1 * str2 =', str1 * 3)

#mengetahui panjang string pakai fungsi len()
# string = "I LOVE PYTHON"
# print(len(string))

#karakter escape, klo mau print string kita tidak bisa menggunakan kutip tunggal, kita bisa pake backflash
#menggunakan kutip tiga 
# print (''' He said, "what's there?"''')
#menggunakan karakter escape untuk tanda kutip tunggal
# print("He said, \"what's there?\"")

# print("Ini adalah baris pertama\nDan ini baris dua")
# print("Ini adalah \x48\x45\x58")

#raw string untung mengabaikan karakter escape
# print("This is \x61\ngood example")
# print(r"This is \x61\ngood example")

#format string (mode format)
#menggunakan posisi default
default_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan Default ---')
print (default_order)