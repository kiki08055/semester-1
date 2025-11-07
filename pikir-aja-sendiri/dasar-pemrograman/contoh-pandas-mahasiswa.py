import pandas as pd

list_nama = []
list_nim = []
list_uts = []
list_uas = []
list_rata = []
list_status = []

jumlah = int(input("Berapa mahasiswa yang ingin diinput: "))

print("\n===== INPUT NILAI MAHASISWA =====")
for i in range(jumlah):
    print(f"\nData ke-{i+1}")
    nim = int(input("NIM        :"))
    nama = input("nama           :")
    uts = int(input("Nilai UTS           :"))
    uas = int(input("Nilai UAS           :"))

    #hitung rata rata
    rata = (uts + uas) / 2
    status = "Lulus" if rata >= 70 else "Tidak lulus"

    #masukkan ke list
    list_nama.append(nama)
    list_nim.append(nim)
    list_uts.append(uts)
    list_uas.append(uas)
    list_rata.append(rata)
    list_status.append(status)

    #membuat data frame
    data = {
        "Nama": list_nama,
        "NIM" : list_nim,
        "UTS" : list_uts,
        "UAS" : list_uas,
        "Rata-rata" : list_rata,
        "Status": list_status
    }

    df = pd.DataFrame(data)

    print("\n=========================================")
    print("              DAFTAR NILAI MAHASISWA      ")
    print("\n=========================================")
    print(df)
    print("\n=========================================")

    df.to_csv("nilai_mahasiswa.csv", index=False)
    print("\nData berhasil disimpan ke: nilai_mahasiswa.csv")