import pandas as pd
name = input("Masukan Nama Pembeli : ")
no_hp = int(input("masukan no hp : "))

# Daftar produk
produk = {
    "P01": {"nama": "mie ayam", "Harga": 20000},
    "P02": {"nama": "mie baso", "Harga": 25000},
    "P03": {"nama": "mie yamin", "Harga": 20000},
    "P04": {"nama": "sate kambing", "Harga": 30000}
}

# Tampilkan daftar produk
print("DAFTAR PRODUK")
for kode, info in produk.items():
    print(f"{kode} - {info['nama']:<12} Rp. {info['Harga']:<12}")

# ===============================
# LIST UNTUK MENYIMPAN BELANJAAN
# ===============================
keranjang = []

banyak_jenis = int(input("\nBanyak jenis produk yang ingin dibeli: "))

for i in range(banyak_jenis):
    print(f"\nJenis ke-{i + 1}")
    kode = input("Masukkan kode produk: ").upper()

    if kode in produk:
        nama = produk[kode]["nama"]
        harga = produk[kode]["Harga"]
        jumlah = int(input("Masukkan jumlah barang: "))

        subtotal = harga * jumlah

        keranjang.append({
            "Kode": kode,
            "Nama Produk": nama,
            "Harga": harga,
            "Jumlah": jumlah,
            "Subtotal": subtotal
        })

        print(f"Ditambahkan: {nama} x{jumlah}")
    else:
        print("Produk tidak ditemukan!")

# ===============================
# DATAFRAME PANDAS
# ===============================
df = pd.DataFrame(keranjang)

# Hitung diskon
df["Diskon"] = df["Subtotal"].apply(
    lambda x: x * 0.10 if x >= 50000 else 0
)

# Hitung pajak
df["Pajak (11%)"] = (df["Subtotal"] - df["Diskon"]) * 0.11

# Total per item
df["Total Akhir"] = df["Subtotal"] - df["Diskon"] + df["Pajak (11%)"]

# ===============================
# STRUK DALAM BENTUK TABEL
# ===============================
print("\n" + "=" * 60)
print("              STRUK PEMBELIAN (PANDAS)")
print("=" * 60)
print(df)

total_bayar = df["Total Akhir"].sum()
print("=" * 60)
print(f"TOTAL BAYAR: Rp {total_bayar:,.0f}")
print("=" * 60)

# ===============================
# PEMBAYARAN
# ===============================
while True:
    bayar = int(input("Masukkan uang pembayaran: Rp "))
    if bayar < total_bayar:
        print(f"Uang kurang Rp {total_bayar - bayar:,.0f}")
    else:
        print("\nPembayaran berhasil")
        print(f"Kembalian: Rp {bayar - total_bayar:,.0f}")
        break

print("=" * 60)
print("Terima kasih sudah berbelanja di Indomart,",name)
print("=" * 60)



while True:
    bayar = int(input("Masukkan uang pembayaran: Rp "))
    if bayar < total_bayar:
        print(f"Uang kurang Rp {total_bayar - bayar:,.0f}")
    else:
        print("\nPembayaran berhasil")
        print(f"Kembalian: Rp {bayar - total_bayar:,.0f}")
        break