def total1(absen, tugas, project):
    akhir = (0.2 * absen) + (0.25 * tugas) + (0.55 * project)
    return akhir

def grade(akhir):
    if akhir >= 70:
        g = "Lulus"
        return g
    elif akhir < 70:
        g = "Gagal"
        return g