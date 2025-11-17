# def sapa(nama):
#     '''fungsi ini untuk menyapa seseorang sesuai yang dimasukkan sebagai parameter'''
#     print("Hi! " + nama + ", Apa kabar")
# sapa("Kiki")

#definisi fungsi print_string
# def print_string(str):
#     '''menampilkan argumen string str ke layar'''
#     print(str)

# #kita memanggil fungsi dengan kata kunci
# print_string(str= "Heloo python")

#DEFINISI FUNGSI 
# def print_info(nama, usia):
#     '''fungsi ini menampilakn info yang dimasukkan'''
#     print("Nama: ", nama)
#     print("Usia: ", usia)

# #memanggil fungsi
# #output
# print_info(usia= 25, nama= "janco")

#DEFINISI FUNGSI
# def print_info(nama, usia= 17):
#     '''fungsi ini menampilakn info yang dimasukkan'''
#     print("Nama: ", nama)
#     print("Usia: ", usia)

# #memanggil fungsi print_info
# print_info(usia= 25, nama= "Galih")

# #pemanggilan fungsi tidak menyediakan argumen usia
# print_info( nama= "Galih")

#tanda asterisk
#Definisi fungsi
# def print_info(argi, *vartuple):
#     '''fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan'''
#     print("Outputnya adalah: ")
#     print(argi)
#     for var in vartuple:
#         print (var)
# #pemanggilan fungsi
# #satu argumen
# print_info(10)

# #empat argumen
# print_info(10,30,50,70)

#variable global
#defini fungsi
def sum(arg1, arg2):
    '''menambahkan variable dan mengembalikan hasilnya'''
    total = arg1 + arg2
    #total disini adalah variable lokal
    print("Di dalam fungsi nilai total: ", total)
    return total

#pemanggilan fungsi sum
hasil = sum(10, 20)
print("Di luar fungsi, nilai total: ", hasil)
    
