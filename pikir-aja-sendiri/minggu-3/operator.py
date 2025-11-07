#mengupdate string, immutable (tidak bisa diubah)
# var1 = 'Hello python'
# var2 = var1[:6]
# print(var1)
# print("String update: -", var2 + 'bank')  

# kata = "aku suka makan pisang"
# update = kata[:15] + "nasi" #variable kata di atas bakal d slice (di index 15(0-15))
# print(kata)
# print(update)
# print(len(kata)) #len itu untuk menghitung index (panjang index)
# print (kata * 3)

# #escape
# # #menggunakan kutip tiga
# print(''' He said, "what's there"''')
# #menggunakan karakter escape untuk tanda kutip tunggal
# print('He said, "what\'s there"')
# #menggunakan tanda kutip ganda
# print("He said, \"What's there?\"")

# print("Hello\nWorld") #escape untuk bisa anu baris baru
# print("Nama:\tKiki") #tab (biar rapih)
# print("Huruf A:", "\x42") #ga penting (soalnya ga ngerti)

#raw string umtuk mengabaikan karakter escape
# print("This is \x61 \ngood example")
# print(r"This is \x61 \ngood example")

#menggunakan posisi default
# default_order = "{}, {} dan {}".format("Kiki", "Acaa", "Bintang")
# print("\n--- Urutan default ---")
# print(default_order)

#menggunakan argument posisi
# positional_order = "{1}, {0} dan {2}".format("kiki", "bintang", "anu") #nyusun nya dari index
# print('\n--- Urutkan berdasarkan posisi ---')
# print (positional_order)

#Format integer
# print("{0} bila diubah jadi binar menjadi {0:b}".format(29))
# #format float
# print("format eksponensial: {0:e}".format(1566.345))
#pembulatan
# print("sepertiga sama dengan: {0:.3f}".format(1/3))
#meratakan string
# print("|{:<10}|{:>10}|{:>10}".format('beras', 'gula', 'garam'))

#FUNGSI BAWAAN STRING
# print("Universitas BIna Sarana Informatika".lower()) #huruf kecil semua
# print("Universitas BIna Sarana Informatika".upper()) #huruf kapital semua
# print("I love programming".split()) #d splitt itu kyk pake array
# print("I love anu".startswith("I")) #memiriksa huruf pertama bener (i), klo iya true,salah false
# print("Saya belajar bintang".endswith("on")) #memeriksa kata terakhir (on), klo iya true, salah ya false bloon
# print(' - '.join(['I', 'love', 'Bintang'])) #buat nambahin karakter atau apapun
# print("Belajar Java di BSI".replace('Java', 'Python')) #kata yang sama bnakal d ganti sama yg baru (kyk people and go eaa)

#Konversi Jenis Bilangan
#bilangan int ke float atau sebalikknya
# print(int(2.5)) #float ke int
# print(int(3.8)) #float ke int
# print(float(5)) #int ke float

#Python Decimal
# print((1.1 + 2.2) == 3.3)
# print(1.1 + 2.2) #outputnya bukan 3.3 d python beda lg karena yg d mengerti kamputer cmn 1 0

#Bilangan Pecahan 
import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(1.3)) 