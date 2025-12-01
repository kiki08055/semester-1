
'''buat contoh variable lokal sama global - dosen pengganti''' 
x = int(input("Masukkan angka x: "))   # ini variabel global

def tampilkan():
    print("Nilai x di dalam fungsi:", x)

tampilkan()
print("Nilai x di luar fungsi:", x)

def hitung():
    y = int(input("Masukkan nilai y : "))   # ini variabel lokal
    print("Nilai y di dalam fungsi:", y)

hitung()
print("Nilai y di luar fungsi:", y)  # erro y tidak dikenal (karena d luar fungsi)

  