import modul
import pandas as pd

name = input("Masukan nama anda : ")
noHp = int(input("Masukan no Handphone : "))

print("=" * 80)
#  DAFTAR PRODUCT 

product = {
    "P01": {"nama": "mie ayam", "harga": 20000},
    "P02": {"nama": "mie indomie", "harga": 150000},
    "P03": {"nama": "mie yamin", "harga": 280000},
    "P04": {"nama": "ayam penyet", "harga": 250000},
    "P05": {"nama": "sate kambing", "harga": 30000},
}

print("\nDAFTAR PRODUCT")
for kode, info in product.items():
    print(f"{kode} - {info["nama"]:<12} Rp {info["harga"]:,}")

# INPUT BELANJA
cart = []
banyak_jenis = int(input("\nBanyak jenis produk yang dibeli: "))

for i in range(banyak_jenis):
    print(f"\nJenis ke-{i+1}")
    kode = input("Masuka kode product: ").upper()

    if kode in product:
        jumlah = int(input("Masukan jumlah: "))
        harga = product[kode]["harga"]
         
        cart.append({
            "Kode" : kode,
            "Nama Produk" : product[kode]["nama"],
            "Harga" : harga,
            "Jumlah" : jumlah,
            "Subtotal" : harga * jumlah
        })
    else:
        print("Produk tidak ditemukan!")

# DATAFRAME

df = pd.DataFrame(cart)

# HITUNG POTONGAN TOTAL

total_belanja = df["Subtotal"].sum()


# IMPORT MODUL 
potongan = modul.hitungPotongan(total_belanja)
df = modul.hitungDiskonPerItem(df, total_belanja, potongan)
df = modul.hitung_pajak_total(df)

#strk
print
("\n" + "=" * 80)
print("                                  STRUK PEMBELIAN")
print("=" * 80)
print(df)

totalBayar = int(df["Total Akhir"].sum())
print(f"Total Belanja   : Rp {total_belanja:,.0f}")
print(f"Total Potongan  : Rp {potongan:,.0f}")
print(f"Total Bayar     : Rp {df["Total Akhir"].sum():,.0f}")
print("=" * 80)

#
# PEMBAYARAN

while True: 
    bayar = int(input("Masukan uang Pembayaran: Rp "))

    if bayar < totalBayar:
        kurang = totalBayar - bayar
        print(f"Uang kurang Rp {kurang:,.0f}")
    else:
        kembalian = bayar - totalBayar
        print("\nPembayarab berhasil")
        print(f"Kembalian: Rp {kembalian:,.0f}")
        break

print(f"Terima kasih sudah berbelanja ditoko kami. {name}")