#Perulangan for
# Looping for: mencetak angka 1 sampai 5
# for i in range(1, 6):
#     print(f"Angka ke-{i}")

# n = int(input("Masukkan angka disini : "))
# for i in range (n):  # i itu sebuah variable, dan perulangan nya 
#     print (i)

#perulangan while akan terus terjadi selma kondisi true
# Looping while: mencetak angka 1 sampai 5
# i = 1
# while i <= 5:
#     print(f"Angka ke-{i}")
#     i += 1  # menambah nilai i setiap perulangan

# n = int(input("Banyak data: "))
# for i in range (n):
#     print (i)

#MENAMPILKAN DERET BILANGAN
# n= int(input("Masukkan nilai n: "))
# x = 2
# while x <= n:
#     print(x, end=" ")
#     x = x + 2

#mencetak angka 1 - 15
# angka = 1
# while angka <= 15:
#     print (angka)
#     angka = angka + 1

#Bilangan menurun
#mencetak angka 10 -1
# bil = 10
# while bil > 0:
#     print (bil)
#     bil = bil - 1

# # Menentukan bilangan prima
# bilangan = int(input("Masukkan Bilangan : "))

# # Bilangan prima harus lebih besar dari 1
# if bilangan > 1:
#     for i in range(2, bilangan):
#         if (bilangan % i) == 0:
#             print(bilangan, "bukan bilangan prima")
#             print(i, "kali", bilangan // i, "=", bilangan)
#             break
#     else:  # <-- ini sejajar dengan 'for', bukan dengan 'if' di dalamnya
#         print(bilangan, "adalah bilangan prima")
# else:
#     print(bilangan, "bukan bilangan prima")

#perintah break pada looping
# bil = 6
# for i in range(0, 10):
#     print(i)
#     if i is bil:
#         break #looping akan d kerjakan terus sampai d paksa keluar oleh intruksi break

#PERINTAH CONTINUE
''' fungsi continue akan melakukan pengulangan
mulai dari awal lagi'''
# bil = 0
# pilihan = 'y'
# while (pilihan != 'n'):
#     bil = int(input("Masukkan bilangan dibawah 50: "))

#     if (bil > 50 ):
#         print ("Bilangan melebihi angka 50, silahkan diulangi.")
#         continue
#     print("Perangkat dua dari bilangan ini adalah: ", bil * bil)
#     pilihan = input("Apakah Anda ingin mengulang kembali (y/n)? ")

#NESTED LOOP
# n = 5
# i = 1
# while n >= i:
#     j = 5
#     while j >= n:
#         print(j, end=" ")
#         j -= 1
#     print()
#     n -= 1

# #mencetak bilangan prima antara 1 sampai 50
# i = 2
# while(i < 50):
#     j = 2
#     while (j <= (i/j)):
#         if not (i/j):
#          j = j + 1
#     if (j > i/j) : print(i,"adalah bilangan prima")
#     i = i + 1
# print ("Terimakasih")

# Mencetak bilangan prima antara 1 sampai 50
# i = 2
# while i <= 50:
#     j = 2
#     while j <= i / j:
#         if i % j == 0:
#             break
#         j = j + 1
#     if j > i / j:
#         print(i, "adalah bilangan prima")
#     i = i + 1

# print("Terima kasih")

#studi kasusu
# for i in range (2,12,2):
#     print(i)

#membuat program menjumlahkan bilangan 1 - 10
# jum = 0
# for i in range(10):
#     i = i + 1
#     print(i)
#     jum = jum + i
# print()
# print("Jumlah Bilangan 1 - 10 adalah: ", jum)

# Program menggambar segitiga siku-siku

# # Meminta input dari pengguna
# n = int(input("Masukkan bilangan bulat (1-100): "))

# # Pastikan input berada dalam rentang yang benar
# if 1 <= n <= 100:
#     for i in range(1, n + 1):
#         print("" * i)
# else:
#     print("Angka harus antara 1 sampai 100!")

# n = int(input("Masukkan bilangan/karakter : "))
# #lakukan perulangan nested for utk mnghslkn pola siku'
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("*", end="")
#     print('')


# n = int(input("Masukkan angka disini : "))
# karakter = input("Masukkan karakter [*/#/%/@/&] : ")
# if 1 <= n <= 100:
#     for i in range(1, n + 1):
#         print(" " * (n - i) + karakter * (2 * i - 1))

# n = int(input("Masukkan angka disini : "))
# print ("="*40)

# if 1 <= n <= 100:
#     print("Tek kotek kotek kotek, anak ayam turun berkotek")
#     for i in range(n, 0, -1):
#         if i > 1:
#          print("anak ayam turunlah", i, "mati satu tinggalah", i - 1)
#         else:
#             print("anak ayam turunlah 1 mati satu tinggallah induknya")