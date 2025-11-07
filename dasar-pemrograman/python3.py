# #string adalah type data karakter
# # var1 = 'Hello Python'
# # var2 = "Programming with python"
# # print (var1)
# # print (var2)

# #substring / ambil nilai
# # var1 = 'Hello Python'
# # var2 = "I love python"
# # print("ambil karakter ke-0", var1[0]) #ngambil index ke 0
# # print("ambil karakter mulai dari 2 sebanyak 6", var2[2:6]) #ngambil 2 sebanyak 6

# #update string
# # var1 = 'Hello python'0
# # var2 = var1[:6]
# # print(var1)
# # print("String update: -", var2 + 'world') 

# #mengtahui panjang string 
# # string = "I love python"
# # print("panjang karakter" , len(string)) 

# #escape
# # #menggunakan kutip tiga, fungsinya agar kitya menegtik tanda petik dalam tanda petik
# # print(''' He said, "what's there"''')
# # #menggunakan karakter escape untuk tanda kutip tunggal
# # print('He said, "what\'s there"')
# # #menggunakan tanda kutip ganda
# # print("He said, \"What's there?\"")

# #HEXA

# # print("Ini adalah baris pertama\nDan ini baris dua")
# # print("Ini adalah \x48\x45\x58") # kalo kamu mengabailkan hexa pake format r

# #menggunakan posisi default
# # default_order = "{}, {} dan {}".format("Kiki", "Acaa", "aisyah")
# # print("\n--- Urutan default ---")
# # print(default_order)

# #menggunakan argument posisi
# # positional_order = "{1}, {0} dan {2}".format("kiki", "aisayh", "anu") #nyusun nya dari index
# # print('\n--- Urutkan berdasarkan posisi ---')
# # print (positional_order)

# #Format integer
# # print("{0} bila diubah jadi binar menjadi {0:b}".format(29))
# # #format float
# # print("format eksponensial: {0:e}".format(1566.345))
# #pembulatan
# # print("sepertiga sama dengan: {0:.3f}".format(1/3)) #3f artinya koita mau pake brp karakter setelah koma
# #meratakan string
# # print("|{:<10}|{:^10}|{:>10}".format('beras', 'gula', 'garam'))

# # x = 12.3456789
# # print("Nilai x adalah = %3.2f" %x)
# # print("Nilai x adalah = %3.4f" %x)

# # #FUNGSI BAWAAN STRING
# # print("Universitas BIna Sarana Informatika".lower()) #huruf kecil semua
# # print("Universitas BIna Sarana Informatika".upper()) #huruf kapital semua
# # print("I love programming".split()) #d splitt itu kyk pake array
# # print("I love anu".startswith("I")) #memiriksa huruf pertama bener (i), klo iya true,salah false
# # print("Saya belajar dudung".endswith("on")) #memeriksa kata terakhir (on), klo iya true, salah ya false bloon
# # print('. '.join(['I', 'love', 'dudung'])) #buat nambahin karakter atau apapun
# # print("Belajar Java di BSI".replace('Java', 'Python')) #kata yang sama bnakal d ganti sama yg baru (kyk people and go eaa) / niban


# #OPERATOR
# #aritmatika 
# n1 =int(input("Masukkan nilai 1 : "))
# n2 =int(input("Masukkan nilai 2 : "))
# # print ("Operator aritmatika")
# # print ("-------------------------------")
# # tambah =  n1 + n2
# # print (n1, "+", n2, "=", tambah)

# # print ("-------------------------------")
# # kurang =  n1 - n2
# # print (n1, "-", n2, "=", kurang)

# # print ("-------------------------------")
# # pangkat =  n1**n2
# # print (n1, "pangkat", n2, "=", pangkat)

# # print ("-------------------------------")
# # sisa =  n1%n2
# # print (n1, "%", n2, "=", sisa)

# # print ("-------------------------------")
# # bulat =  n1 // n2
# # print (n1, "//", n2, "=", bulat)

# print ("-------------------------------")
# kali =  n1 * n2
# print (n1, "*", n2, "=", kali)

# print ("-------------------------------")
# bagi =  n1 / n2
# print (n1, "/", n2, "=", bagi)

# # print ("OPERATOR RELASI")
# kurang = n1 < n2
# print (n1, "<", n2, "=", kurang)
# print ("-------------------------------")

# lebih = n1 > n2
# print (n1, ">", n2, "=", lebih)
# print ("-------------------------------")

# sama = n1 == n2
# print (n1, "==", n2, "=", sama)
# print ("-------------------------------")

# taksama = n1 != n2
# print (n1, "!=", n2, "=", sama)
# print ("-------------------------------")


# #operator logika
# op_and = n1 > n2 and n1 < n2
# print(n1, ">", n2, "AND", n1, "<", n2, "=", op_and )
# print ("-------------------------------")

# op_or = lebih or kurang
# print(n1, ">", n2, "AND", n1, "<", n2, "=", op_or )
# print ("-------------------------------")