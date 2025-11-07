# def pangkat (x,y): #def itu definisi pemberian
#     if y == 0:
#         return 1
#     else:
#         return x * pangkat(x, y-1)

# x = int(input("Masukkan Nilai X : "))
# y = int(input("Masukkan Nilai Y : ")) #y ini pangkat

# print("%d dipangkatkan %d = %d" % (x, y, pangkat(x, y)))

#faktorial
# def faktorial(a):
#     if a == 1:
#         return (a)
#     else :
#         return (a*faktorial(a-1))
    
# bil = int(input("Masukkan bilangan : "))

# print("%d! = %d" % (bil, faktorial(bil)))

#DERET FIBONANCY 
def fibonacci (n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n-2))
    
x = int(input("Masukkan Batas Deret bilangan Fibonacci : "))
print("Deret Fibonacci")
for i in range (x):
    print (fibonacci(i), end=" ")