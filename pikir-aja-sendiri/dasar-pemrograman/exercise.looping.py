# #ini pakai list
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


print("=" * 40)
print("      PROGRAM KASIR SEDERHANA")
print("=" * 40)

total = 0
no = 0

# User tentukan berapa jenis produk
banyak_jenis = int(input("Banyak jenis produk yang ingin dibeli: "))

# Input produk sesuai jumlah jenis
for i in range(banyak_jenis):
    no += 1
    print(f"\nMasukkan barang ke - {no}")
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    
    subtotal = harga * jumlah
    total += subtotal
    print(f"Subtotal       : {subtotal}")
    print(f"Total sementara: {total}")

# Opsi untuk tambah barang lagi setelah jenis awal
while True:
    lagi = input("\nMasukkan barang lagi? (y/n): ")
    if lagi.lower() == "n":
        break

    no += 1
    print(f"\nMasukkan barang ke - {no}")
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    
    subtotal = harga * jumlah
    total += subtotal
    print(f"Subtotal       : {subtotal}")
    print(f"Total sementara: {total}")

# Setelah semua barang diinput, tampil total akhir
print("\n" + "=" * 40)
print(f"Total yang harus dibayar: Rp{total}")
print("=" * 40)

# Pembayaran (kalau kurang, disuruh ulang)
while True:
    uang = int(input("Masukkan uang pembayaran: Rp"))
    if uang < total:
        print(f"Uang Anda kurang Rp{total - uang}. Silakan masukkan ulang.")
    else:
        print(f"Sisa uang Anda: Rp{uang - total}")
        print("Terima kasih telah berbelanja!")
        break
