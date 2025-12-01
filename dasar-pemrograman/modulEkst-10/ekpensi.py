# angka1 = int(input("Masukkan angka 1: "))
# angka2 = int(input("Masukkan angka 2: "))
# bagi = angka1 / angka2
# print("hasil: ", bagi)


# try:
#     angka1 = int(input("Masukkan angka 1: "))
#     angka2 = int(input("Masukkan angka 2: "))
#     bagi = angka1 / angka2
#     print("hasil: ", bagi)
# except ValueError:
#     print("Error: inputan harus angka")

# except ZeroDivisionError:
#     print("Error: GA BOLEH 0!!!")
# finally:
#     print("program selesai")

# try:
# # lakukan sesuatu pass
# except ValueError:
# # tangani eksepsi ValueError pass
# except (TypeError, ZeroDivisionError): # menangani multi eksepsi
# # TypeError dan ZeroDivisionError pass
# except:
# # menangani eksepsi lainnya
# pass

# try:
#     a = int(input("Masukkan sebuah bilangan positif: "))
#     if a <= 0:
#         raise ValueError("itu bukan bilangan positif! ")
# except ValueError as ve : print (ve)

try:
    x = int(input("Masukkan angka: "))
    print("Kuadrat:", x * x)

except ValueError:
    print("Input harus berupa angka!")

except TypeError:
    print("Terjadi kesalahan tipe data!")
