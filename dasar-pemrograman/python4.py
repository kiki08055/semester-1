# #PERCABANGAN 
#if sederhana
# nilai = 70
# if nilai > 80:
#     print("Anda lulus")

# #   IF ELSE 
# angka = 7
# if angka > 0 :
#     print ("Bilangan bulat")
# else:
#     print ("Bilangan negatif")

# #IF ELIF ELSE 
# kode = "001"
# if kode =="001":
#     print ("Nama Barang pensil")
# elif  kode == "002":
#     print ("Nama Barang Buku")
# else :
#     print ("Anda Salah Kode")

# #NESTED IF
# #contoh 2
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

#Program Ganjil Genap
# print ("      Pogram Ganjil-Genap")
# print ("="* 40)
# nilai = int(input("Masukkan Angka Disini : "))
# if nilai % 2 == 0 :
#     print ("Bilangan yang anda masukkan adalah bilangan Genap ")
# else :
#     print ("Bilangan yang anda masukkan adalah bilangan Ganjil ")

#TIKET BUS

nama = input("Masukkan Nama Pembeli : ")
noHp = input("Masukkan no hp : ")
kodeJur = input ("Masukkan Jurusan [SBY/BL/LMP]")
jumlahBeli = int(input("Maasukkan Jumlah Beli : "))

#proses
if kodeJur =="SBY" or kodeJur == "sby":
    kota = "Surabaya"
    harga = 300000
elif kodeJur == "BL" or kodeJur == "bl":
    kota = "Bali"
    harga = 400000
elif kodeJur == "LMP" or kodeJur == "LMP":
    kota = "Lampung"
    harga = 500000
else :
    kota = "Salah kode"
    harga = 0

if jumlahBeli >= 3 :
    diskon =(0.1*jumlahBeli*harga)
else:
    diskon = 0

totalBayar = (harga * jumlahBeli) - diskon

print ("=" * 40)
print ("PENJUALAN TIKET BUS")
print ("="*40)
print ("Nama pembeli\t: ", nama)
print ("No Hp\t: ", noHp)
print ("Kode Jurusan\t: ", kodeJur)
print ("Kota Tujuan\t: ", kota)
print ("Jumlah Tiket\t: ", jumlahBeli)
print ("Harga Tiket\t: ", harga)
print ("Diskon\t: ", diskon)
print ("Total Bayar\t: ", totalBayar)
ubay=int(input("Masukkan Uang Bayar : "))
ukem = ubay - totalBayar
print ("Uang kembali\t : ", ukem)