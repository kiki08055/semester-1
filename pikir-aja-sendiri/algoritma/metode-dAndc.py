# # binary search
# def BinSearch(data, key):
#     awal = 1
#     akhir = len(data) + 1
#     ketemu = False
#     while (awal <= akhir) and not ketemu:
#         tengah = int((awal + akhir)/2)
#         if key == data[tengah]:
#             ketemu = True
#             print('data', key, 'ditemukan posisi', tengah+1)
#         elif key < data [tengah]:
#             akhir = tengah - 1
#         else:
#             awal = tengah + 1
#     if not ketemu:
#         print('data tidak ditemukan')

# data = [1, 3, 9, 11, 15, 22, 29, 31, 48]
# BinSearch(data, 3)

# MERGE SORT
def mergeSort(x):
    print("Bilangan diurutkan ", x)
    if len(x) > 1:

        mid = len(x) // 2
        lefthalf = x[:mid]
        righthalf = x[mid:]

        #rekursif
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        # proses perbandingan
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                x[k] = lefthalf[i]
                i=i+1
            else:
                x[i] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len (lefthalf):
            x[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            x[k] = righthalf[j]
            j= j + 1
            k= k + 1
            print("Merging ", x)

x = [22, 10, 15, 3, 8, 2]
mergeSort(x)
print (x)

