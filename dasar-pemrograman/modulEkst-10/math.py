# from math import factorial

# bill = int(input("Masukkan sebuah bilangan positif : "))
# faktorial_bill = factorial(bill)
# print("Bilangan faktorial dari bill adalah: ", faktorial_bill)

# from math import pow

# pangkat_bilangan = pow(3, 3)
# print("Hasil pemangkatan bilangan adalah : ", pangkat_bilangan)

#angka 3 pertama merupakan angka yang akan dipangkatkan
#angka 3 berikutnya adalah jumlah pemangkatan

# from math import*
# pangkat_bilangan = pow(3, 3)
# print("Hasil dari pemangkatan bilangan adalah : ", pangkat_bilangan)

# bil = int(input("Masukkan sebuah bilangan positif: "))
# faktorial_bil = factorial(bil)
# print("Bilangan faktorial dari bil adalah : ", faktorial_bil)

import sys

lists = ['a', 0, 4]
for each in lists:
    try:
        print("masukkan:", each)
        r = 1/int(each)
        break
    except:
        print("Upps!", sys.exc_info()[0], "terjadi.")
        print("Masukkan berikutnya")
        print()
print("kembalikan dari ", each, "= ", r)