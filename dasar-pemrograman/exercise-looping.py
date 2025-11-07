total=0
no=0
while True:
    no=no+1
    print(f"masukan barang ke - {no}")
    nama=input("masukan nama barang: ")
    harga=int(input("masukan harga barang: "))
    jumlah=int(input("masukan jumlah barang: "))
    
    print ("=" * 40)
    subtotal=harga*jumlah
    total = total + subtotal 
    print(f"subtotal       : {subtotal}")
    print(f"total sementara:{total}")
    
    print("=" * 40)
    lagi=input("masukan lagi:(y/n)")
    if lagi.lower() == "n":
        break
print("pembayaran")
print("=" * 40)
uang=int(input("masukan uang: ")) 
if uang < total :
    print("maaf uang anda tidak cukup")  
else:
    print(f"sisa uang anda {uang - total}")
print("terimakasi")