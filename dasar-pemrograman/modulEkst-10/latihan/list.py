import pandas as pd
import modulnya
#variable yg berulang menggunakan list/matriks

list_nim = []
list_nama = []
list_tugas = []
list_project = []
list_total = []
list_absensi = []

ulang = 2
for i in range (ulang):
    print ("data ke - " + str(i+1))
    list_nim.append(input("Nim : "))
    list_nama.append(input("Nama : "))
    list_project.append(int(input("Nilai project : ")))
    list_tugas.append(int(input("Nilai TUGAS : ")))
    list_absensi.append(int(input("Nilai TUGAS : ")))
#proses
 
for i in range (ulang):
    list_total.append(modulnya.total1(list_project [i],list_tugas[i],list_absensi [i]))
    

data = {
    "NIM" : list_nim,
    "Nama Lengkap" : list_nama,
    "Nilai Tugas" : list_tugas,
    "Nilai Project" : list_project,
    "Nilai Absensi" : list_absensi,
    "Rata-rata" : list_total
}
data_siswa = pd.DataFrame(data)
#Cetak
print("================================== Daftar Nilai ================================== ")
print(data_siswa)
print(modulnya.total1)
print("="*90)