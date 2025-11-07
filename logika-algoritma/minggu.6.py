# def pangkat (x,y): #def itu definisi pemberian
#     if y == 0:
#         return 1
#     else:
#         return x * pangkat(x, y-1)

# x = int(input("Masukkan Nilai X : "))
# y = int(input("Masukkan Nilai Y : ")) #y ini pangkat

# print("%d dipangkatkan %d = %d" % (x, y, pangkat(x, y)))

# #faktorial
# def faktorial(a):
#     if a == 1:
#         return (a)
#     else :
#         return (a*faktorial(a-1))
    
# bil = int(input("Masukkan bilangan : "))

# print("%d! = %d" % (bil, faktorial(bil)))

# #DERET FIBONANCY 
# def fibonacci (n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return (fibonacci(n - 1) + fibonacci(n-2))
    
# x = int(input("Masukkan Batas Deret bilangan Fibonacci : "))
# print("Deret Fibonacci")
# for i in range (x):
#     print (fibonacci(i))


# def deret (n):
#     if n == 0:
#         return 0
#     else:
#         return n + deret(n -1)
    
# n = int(input("Masukkan anka : "))

# def deret (n):
#     if n == 0:
#         return n
#     else:
#         return n + deret (n -1)
    
# n = int(input("Masukkan Batas Deret bilangan Fibonacci : "))
# deretj = deret (n)
# hasil = sum(deret)

# print ("Deret penjumlahan : ", deret)
# print ("Penjumlahan nya adalah =", hasil)

# def sumList(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sumList(lst[1:])

# # Data list
# my_list = [1, 8, 3, 10, 2]

# print("=" * 40)
# print("Program Penjumlahan Elemen List (Rekursif)")
# print("=" * 40)
# print(f"List angka: {my_list}")
# print(f"Deret penjumlahan = {sumList(my_list)}")
# print("=" * 40)

# def hit_mundur(n):
#     if n <= 0:
#         print("Selesai")
#     else:
#         print (n)
#         hit_mundur(n-1)
# hit_mundur(5)