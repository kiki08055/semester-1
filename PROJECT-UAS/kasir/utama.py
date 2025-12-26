import pandas as pd

#input user ( data diri )
name = input("Masukan nama anda : ")
noHp = int(input("Masukan no Hp : "))


#list product yang ada
product = { 
    "P01" : {"nama" : "mie ayam", "Harga" : 20000 },
    "P02" : {"nama" : "mie baso", "Harga" : 25000 },
    "P03" : {"nama" : "mie yamin", "Harga" : 20000 },
    "P04" : {"nama" : "sate kambing", "Harga" : 30000 }
}

#keranjang untuk penyimpanan sementara sebelum di proses
cart = {}

print("===== Selamat Datang di Toko ARA ARA RAWWWWR =====")
print("Daftar Product: ")

#tampilkan product nya pake looping bos
for nama, harga in product.items():
    print(f"- {nama} : Rp{harga}")

while True:
    pilih = input("Masukan nama product yang ingin dibeli")

    if pilih == "selesai":
        break

    if pilih in product:
        jumlah = int(input("Masukan jumlah (pilihan) yang ingin dibeli: "))

        if pilih in cart:
            cart[pilih] += jumlah
        else:
            cart[pilih] = jumlah 

        print(f"{jumlah} {pilih} ditambahkan ke keranjang.")

    else:
        print("Product tidak tersedia")

