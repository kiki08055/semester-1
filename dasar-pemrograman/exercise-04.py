# #HITUNG GAJI KARYAWAN
# gaji = 300000
# nama = input("Masukkan nama anda disini : ")
# pendidikan = input ("Masukkan pendidikan : ")
# golongan_jabatan = int (input("Masukkan golongan jabatan [1, 2, 3] : "))
# jam_kerja = int (input("Masukkan jam kerja : "))

# #menentukan tunjangan jabatan
# if golongan_jabatan == 1:
#     tunjangan_jabatan = 0.5 * gaji
# elif golongan_jabatan == 2:
#     tunjangan_jabatan = 0.10 * gaji
# elif golongan_jabatan == 3:
#     tunjangan_jabatan = 0.15 * gaji
# else:
#     tunjangan_jabatan = 0
#     print ("Golongan tidak valid")

# #menentukan tunjangan pendidikan
# if pendidikan == "SMA" or pendidikan == "sma":
#     tunjangan_pendidikan = 0.025 * gaji
# elif pendidikan == "D1" or pendidikan == "d1":
#     tunjangan_pendidikan = 0.05 * gaji
# elif pendidikan == "D3" or pendidikan == "d2" :
#     tunjangan_pendidikan = 0.20 * gaji
# elif pendidikan == "S1" or pendidikan == "s1" :
#     tunjangan_pendidikan = 0.30 * gaji
# else :
#     tunjangan_pendidikan = 0
#     print ("Pendidikan tidak valid!")

# #honor lembur
# if jam_kerja > 8:
#     honor_lembur = (jam_kerja - 8) * 3500
# else:
#     honor_lembur = 0

# #total gaji
# totalGaji = gaji + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# print ("-" * 40)
# print ("         PROGRAM HITUNG GAJI KARYAWAN   ")
# print ("-" * 40)
# print ("Nama Karyawan \t : ", nama)
# print ("Golongan Jabatan : ", golongan_jabatan)
# print ("Pendidikan       : ", pendidikan)
# print ("Jumlah Jam Kerja : ", jam_kerja)
# print ("-" * 40)
# print (f"Tunjangan Jabatan\t : Rp {tunjangan_jabatan:,.2f}")
# print (f"Tunjangan Pendidikan\t : Rp {tunjangan_pendidikan:,.2f}")
# print (f"Honor Lembur\t : Rp {honor_lembur:,.2f}")
# print ("-" * 40)
# print (f"Total Gaji\t : Rp {totalGaji:,.2f}")
# print ("-" * 40)

#TUGAS 2 
#KASIR

print ("=" * 50)
total_belanja = int(input("Masukkan Total Belanja Anda (Rp): "))
member = input("Aapakah Anda Member (y/t) ").lower()

#potongan harga sesuai total belanja
if total_belanja <= 50000:
    potongan = 0
elif total_belanja < 100000:
    potongan = 0.05 * total_belanja
elif total_belanja < 200000:
    potongan = 0.10 * total_belanja
else:
    potongan = 0.20 * total_belanja

#tambahan potongan member
potongan_member = 0
if member == "y" or member == "Y":
    potongan_member = 0.05 * total_belanja

#total semua potongan
total_potongan = potongan + potongan_member

#total bayar
total_bayar = total_belanja - total_potongan

print("\n==============================================")
print ("                STRUK PEMBAYARAN               ")
print("==============================================")
print (f"Total Belanja : Rp{total_belanja:,.2f}")
print (f"Status Member : { 'Ya' if member == 'y' else 'Tidak'}")
print (f"Potongan Belanja : Rp{potongan:,.2f}")
print (f"Potongan Member : Rp{potongan_member:,.2f}")
print("\n==============================================")
print (f"Total Potongan : Rp{total_potongan:,.2f}")
print (f"Total Bayar : Rp{total_bayar:,.2f}")
print("\n==============================================")

#Pesan tambahan
if member == 'y' or member == "Y":
    print("Terimakasih sudah menjadi member kami")
else:
    print("Terimakasih sudah berbelanja")
print("\n==============================================")