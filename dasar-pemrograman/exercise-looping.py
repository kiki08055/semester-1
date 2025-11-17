# total=0
# no=0
# while True:
#     no=no+1
#     print(f"masukan barang ke - {no}")
#     nama=input("masukan nama barang: ")
#     harga=int(input("masukan harga barang: "))
#     jumlah=int(input("masukan jumlah barang: "))
    
#     print ("=" * 40)
#     subtotal=harga*jumlah
#     total = total + subtotal 
#     print(f"subtotal       : {subtotal}")
#     print(f"total sementara:{total}")
    
#     print("=" * 40)
#     lagi=input("masukan lagi:(y/n)")
#     if lagi.lower() == "n":
#         break
# print("pembayaran")
# print("=" * 40)
# uang=int(input("masukan uang: ")) 
# if uang < total :
#     print("maaf uang anda tidak cukup")  
# else:
#     print(f"sisa uang anda {uang - total}")
# print("terimakasi")


total = 0 
no = 0

print (" ======= PROOGRAM KASIR ======= ")

while True:
    no += 1
    print(f"\nBARANG KE - {no}")
    nama = input("NAMA BARANG :")
    harga= int(input("HARGA    : RP "))
    jumlah=int(input("JUMLAH   : "))

    subtotal = harga * jumlah
    total += subtotal

    print (f"SUBTOTAL      : RP {subtotal}")
    print(f"TOTAL SEMENTARA  : RP {total}")

    lagi = input("\nINPUT BARANG LAGI? (Y/N) : ")
    if lagi.lower() == "n":
        break

print("\n==== TOTAL AKHIR ====")
print(f"Jumlah barang : {no}")
print(f"Total belanja : Rp {total}")

uang = int(input ("Masukkan pembayaran : Rp "))
if uang < total:
    print ("Uang anda tidak cullup!")
else:
    kembalian = uang - total
print (f"Kembalian : Rp {kembalian}")
print("\nTerima kasih sudah berbelanja! ")