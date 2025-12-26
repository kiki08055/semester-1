import pandas as pd

print("=" * 50)
name = input("Masukan Nama Pembeli : ")
noHp = int(input("Masukan No Handphone : "))

# ===============================
# DAFTAR PRODUK
# ===============================
produk = {
    "P01": {"nama": "mie ayam", "Harga": 20000},
    "P02": {"nama": "mie baso", "Harga": 25000},
    "P03": {"nama": "mie yamin", "Harga": 20000},
    "P04": {"nama": "sate kambing", "Harga": 30000}
}

print("\nDAFTAR PRODUK")
for kode, info in produk.items():
    print(f"{kode} - {info['nama']:<12} Rp {info['Harga']:,}")

# ===============================
# INPUT BELANJA
# ===============================
keranjang = []
banyak_jenis = int(input("\nBanyak jenis produk yang dibeli: "))

for i in range(banyak_jenis):
    print(f"\nJenis ke-{i+1}")
    kode = input("Masukkan kode produk: ").upper()

    if kode in produk:
        jumlah = int(input("Masukkan jumlah: "))
        harga = produk[kode]["Harga"]

        keranjang.append({
            "Kode": kode,
            "Nama Produk": produk[kode]["nama"],
            "Harga": harga,
            "Jumlah": jumlah,
            "Subtotal": harga * jumlah
        })
    else:
        print("Produk tidak ditemukan!")

# ===============================
# DATAFRAME
# ===============================
df = pd.DataFrame(keranjang)

# ===============================
# HITUNG POTONGAN TOTAL
# ===============================
total_belanja = df["Subtotal"].sum()

if total_belanja <= 50000:
    potongan = 0
elif total_belanja < 100000:
    potongan = 0.05 * total_belanja
elif total_belanja < 200000:
    potongan = 0.10 * total_belanja
else:
    potongan = 0.20 * total_belanja

# ===============================
# BAGI POTONGAN KE TIAP ITEM
# ===============================
df["Diskon"] = (df["Subtotal"] / total_belanja) * potongan

# ===============================
# PAJAK & TOTAL AKHIR (PER ITEM)
# ===============================
df["Pajak (11%)"] = (df["Subtotal"] - df["Diskon"]) * 0.11
df["Total Akhir"] = df["Subtotal"] - df["Diskon"] + df["Pajak (11%)"]

# ===============================
# STRUK
# ===============================
print("\n" + "=" * 60)
print("               STRUK PEMBELIAN")
print("=" * 60)
print(df)
print("=" * 60)

total_bayar = int(df["Total Akhir"].sum())
print(f"Total Belanja   : Rp {total_belanja:,.0f}")
print(f"Total Potongan  : Rp {potongan:,.0f}")
print(f"Total Bayar     : Rp {df['Total Akhir'].sum():,.0f}")
print("=" * 60)

# ===============================
# PEMBAYARAN
# ===============================
while True:
    bayar = int(input("Masukkan uang pembayaran: Rp "))

    if bayar < total_bayar:
        kurang = total_bayar - bayar
        print(f"Uang kurang Rp {kurang:,.0f}")
    else:
        kembalian = bayar - total_bayar
        print("\nPembayaran berhasil")
        print(f"Kembalian: Rp {kembalian:,.0f}")
        break


print(f"Terima kasih sudah berbelanja, {name}")