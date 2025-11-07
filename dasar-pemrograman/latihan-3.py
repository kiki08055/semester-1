#Program toko mainan 
print ("     TOKO MAINAN ANAK")
print ("=" * 40)
name = input ("Masukkan Nama Pembeli : ")
kode_mainan = input ("Masukkan Kode Mainan : ")
harga = int(input("Masukkan Harga : "))
jumlahBeli = int(input("Masukkan jumlah yang di beli : "))

#proses
subtotal = harga * jumlahBeli
ppn = 0.12 * subtotal
total = subtotal + ppn

print ("=" * 40)
print (f"Nama pembeli\t : {name}" )
print (f"Kode Mainan\t : {kode_mainan} " )
print (f"Harga\t : Rp{harga}" )
print (f"Jumlah\t : {jumlahBeli} " )
print (f"PPN\t : Rp{ppn:,.2f}")
print (f"Total\t : RP{total:,.2f} ")



















#REHAN VERSI
# print("Toko Mainan Anak")
# print("=" * 40)

# # Input data pembelian
# nama = input("Masukkan Nama Pembeli : ")
# kode_mainan = input("Masukkan Kode Mainan : ")
# harga = int(input("Masukkan Harga Satuan : "))
# jumlah = int(input("Masukkan Jumlah Beli : "))

# print("=" * 40)

# # Proses perhitungan
# subtotal = harga * jumlah
# ppn = subtotal * 0.12
# total_bayar = subtotal + ppn

# # Output hasil
# print(f"Nama Pembeli\t: {nama}")
# print(f"Kode Mainan\t: {kode_mainan}")
# print(f"Harga Satuan\t: Rp{harga:,}")
# print(f"Jumlah Beli\t: {jumlah}")
# print(f"Subtotal\t: Rp{subtotal:,}")
# print(f"PPN (12%)\t: Rp{ppn:,.2f}")+
# print(f"Total Bayar\t: Rp{total_bayar:,.2f}")

# print("=" * 40)
# print("Terima kasih sudah berbelanja di Toko Mainan Anak!")