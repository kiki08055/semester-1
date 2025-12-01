# #program hitung gaji karyawan

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
print ("            STRUCK INDOMART")
print("=" * 40)

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