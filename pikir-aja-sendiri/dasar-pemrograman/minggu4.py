#kalo bilangan positif, tampilkan pesan
# angka = -5
# if angka > 0:
#     print(angka, "adalah bilangan positif.")
# else :
#     print(angka, "ini negatif.")
    
# angka = 2
# #yang berikut akan bernilai false sehingga tidak di eksekusi
# if angka > 0:
#     print(angka, "adalah bilangan positif.")
# print ("--------------------------------------------")

#pemrograman menguji apakah sebuah bilangan positif atau negatif
#dan menampilkan pesan ke monitor

# bilangan = 8

# #coba juga mengubah bilanagn menjadi = -1

# if bilangan >= 0:
#     print("Positif atau nol")
# else :
#     print("Bilangan negatif")

# print ("--------------------------------------")

#IF ELIF ELSE

# '''disini kita menguji apakah sebuah bilangan adalah bilangan positif,nol, atau negatif
# dan menampilkan hasilnya '''

# bilangan = 5.5

# '''coba juga mengganti bilangan jadi
# bilangan = 0
# bilangan = -5.5 '''

# if bilangan > 0:
#     print("Bilangan positif")
# elif bilangan == 0 :
#     print("Nol")
# else :
#     print ("Bilangan negatif")
# print ("------------------------------------------")

#contoh 2
# kode_baju = input("Masukkan kode Baju [SP/AD] : ")
# ukuran = input("Masukkan Ukuran Baju [S/M] : ")

# #elif pertama, buat merk superOry/SP
# #elif kedua buat adidas/AD
# if kode_baju == "SP" or kode_baju == "sp" :
#     merk = "SuperOry"
#     if ukuran == "S" or ukuran == "s" :
#         harga = 45000
#     elif ukuran == "M" or ukuran == "m" :
#         harga = 50000
#     else:
#         harga = 0
# elif kode_baju == "AD" or kode_baju == "ad" : 
#     merk = "Adidas"
#     if ukuran == "S" or ukuran == "s" :
#         harga = 65000
#     elif ukuran == "M" or ukuran == "m" :
#         harga = 70000
#     else:
#         harga = 0

# else :
#     merk = "Anda Salah input Kode merk"
#     harga = 0

# print ("--------------------------")
# print ("Merk baju : "+str(merk))
# print ("Harga Baju : Rp.", harga)

#STUDI KASUS ada 2 insyallah kalo mut aku buat sendiri
# nama_pembeli = input ("Masukkan nama anda : ")
# no_hp = input ("Masukkan no hp anda : ")
# kode_jurusan = input ("Masukkan kode jurusan [SBY/BL/LMP] ")
# jumlah_tiket = int(input("Masukkan jumlah tiket : "))

# pembeli = input ("Input nama pembeli : ")
# no_hp = input ("Input no. Handphone : ")
# jurusan = input ("Input Jurusan [SBY/BL/LMP] : ")
# #PROSES
# if jurusan == "SBY" or jurusan == "sby": 
#     namaJurusan = "Surabaya"
#     harga =300000
# elif jurusan == "BL" or jurusan == "bl":
#     namaJurusan = "Bali"
#     harga = 400000
# else :
#     namaJurusan = "Lampung" or jurusan == "lmp"
#     harga = 500000

# #input jumlah beli
# jumlah = int(input("Masukkan Jumlah Beli : "))

# #proses potongan
# if jumlah >= 3 :
#     potongan = (jumlah * harga)*0.1
# else: 
#     potongan = 0

# total =(jumlah*harga) - potongan

# print ("-----------------------------------")
# print ("            PENJUALAN TIKET BUS")
# print ("                   XYZ")
# print ("-----------------------------------")
# print (f"Nama pembeli : "+str(pembeli))
# print (f"No. Handphone : "+str(no_hp))
# print (f"Kode Jurusan yang dipilih : "+str(jurusan))
# print (f"Nama Kota Tujuan : "+str(namaJurusan))
# print (f"Harga : ",(harga))
# print (f"Jumlah Beli : ",+(jumlah))
# print ("-----------------------------------")
# print (f"Potongan yang didapat ",+(potongan))
# print (f"Total bayar : ",+(total))
# ubay= int(input("Masukkan Uang Bayar : "))
# uangKembali=ubay-total
# print("Uang Kembali : ", uangKembali)

#Latihan studi kasusu pendaftaran mahasiswa
# nama_mahasiswa = input("Input nama mahasiswa : ")
# nim = input("Input NIM : ")
# kode_jurusan = input("Input kode jurusan [SI/SIA] : ")

# # proses menentukan jurusan dan harga
# if kode_jurusan == "SI" or kode_jurusan == "si":
#     namaJurusan = "Sistem Informasi"
#     harga = 2400000
# elif kode_jurusan == "SIA" or kode_jurusan == "sia":
#     namaJurusan = "Sistem Informasi Akuntansi"
#     harga = 2000000
# else:
#     namaJurusan = "Kode jurusan tidak valid"
#     harga = 0

# # output hasil
# print("-----------------------------------")
# print("         DAFTAR MAHASISWA BARU")
# print("-----------------------------------")
# print("Nama Mahasiswa : ", nama_mahasiswa)
# print("NIM            : ", nim)
# print("Kode Jurusan   : ", kode_jurusan)
# print("Program Studi  : ", namaJurusan)
# print("Biaya Kuliah   : Rp", format(harga, ","))
# print("-----------------------------------")

#program hitung gaji karyawan

# gaji = 3000000
# nama = input ("Masukkan nama karyawan : ")
# pendidikan = input ("Masukkan pendidikkan : ")
# golongan_jabatan = int( input ("Masukkan golongan jabatan : "))
# jam_kerja = int (input ("Masukkan jam kerja : "))

# #menetukan tunjangan jabatan
# if golongan_jabatan == 1:
#     tunjanganJabatan = 0.5 * gaji
# elif golongan_jabatan == 2 :
#     tunjanganJabatan = 0.10 * gaji
# elif golongan_jabatan == 3:
#     tunjanganJabatan = 0.15 * gaji
# else :
#     tunjanganJabatan = 0
#     print("Golongan tidak valid")

# #menentukan tunjangan pendidikkan 
# if pendidikan == "SMA" or pendidikan == "sma":
#     tunjanganPendidikan = 0.025 * gaji
# elif pendidikan == "D1" or pendidikan == "d1":
#     tunjanganPendidikan = 0.05 * gaji
# elif pendidikan == "D3" or pendidikan == "d3":
#     tunjanganPendidikan = 0.20 * gaji
# elif pendidikan == "S1" or pendidikan == "s1":
#     tunjanganPendidikan = 0.30 * gaji
# else :
#     tunjanganPendidikan = 0
#     print ("Pendidikan tidak valid!")

# #menghitung honor lembur
# if jam_kerja >= 8:
#     honor_lembur = (jam_kerja - 8 ) * 3500
# else:
#     honor_lembur = 0

# #total gaji
# totalGaji = gaji + tunjanganJabatan + tunjanganPendidikan + honor_lembur

# print ("-----------------------------------------------------")
# print ("                    PROGRAM HITUNG GAJI KARYAWAN     ")
# print ("-----------------------------------------------------")
# print ("Nama Karyawan         : ", nama )
# print ("Golongan Jabatan      : ", golongan_jabatan )
# print ("Pendidikan            : ", pendidikan )
# print ("Jumlah Jam Kerja      : ", jam_kerja ) 
# print ("-----------------------------------------------------")
# print (f"Tunjangan Jabatan\t : Rp {tunjanganJabatan:,.2f}")
# print (f"Tunjangan Pendidikan\t : Rp {tunjanganPendidikan:,.2f}")
# print (f"Honor Lembur\t: Rp {honor_lembur:,.2f}")
# print ("-----------------------------------------------------")
# print (f"Total Gajit\t: Rp {totalGaji:,.2f}" )
# print ("-----------------------------------------------------")

print("=" * 40)

nama = input("Masukkan Nama Pembeli : ")
total_belanja = int(input("Masukkan Total Belanja Anda (Rp): "))
member = input("Apakah Anda Member (y/t)? ").lower()

# Menentukan potongan harga berdasarkan total belanja
if total_belanja < 50000:
    potongan = 0
elif total_belanja < 100000:
    potongan = 0.05 * total_belanja
elif total_belanja < 200000:
    potongan = 0.10 * total_belanja
else:
    potongan = 0.15 * total_belanja

# Tambahan potongan untuk member
potongan_member = 0
if member == "y":
    potongan_member = 0.05 * total_belanja

# Total semua potongan 
total_potongan = potongan + potongan_member

# Hitung total bayar
total_bayar = total_belanja - total_potongan

# Cetak struk
print("\n=====================================")
print("           STRUK PEMBAYARAN          ")
print("=====================================")
print(f"Nama Pembeli  : {nama}")
print(f"Status Member : {'Ya' if member == 'y' else 'Tidak'}")
print("-------------------------------------")
print(f"Total Belanja : Rp{total_belanja:,.2f}")
print(f"Potongan Belanja : Rp{potongan:,.2f}")
print(f"Potongan Member  : Rp{potongan_member:,.2f}")
print("-------------------------------------")
print(f"Total Potongan   : Rp{total_potongan:,.2f}")
print(f"Total Bayar      : Rp{total_bayar:,.2f}")
print("=====================================")

# Pesan tambahan
if member == "y":
    print("Terima kasih sudah menjadi member setia kami!")
else:
    print("Terima kasih sudah berbelanja")

print("=====================================")




