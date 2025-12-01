# #MERGE SORT (LANJUTAN)
# def margeSort(x):
#     print("Bilangan diurutkan", x)
#     if len(x)>1:

#         mid = len(x)//2
#         lefthalf = x[:mid]
#         righthalf = x[mid:]

#         # rekursi
#         margeSort(lefthalf)
#         margeSort(righthalf)

#         i= j = k = 0

#         # proses perbandingan dan penggabungan
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 x[k]=lefthalf[i]  ##k itu sebagai penengah
#                 i = i + 1
#             else:
#                 x[k]= righthalf[j]
#                 j = j+1
#             k= k + 1

#         # salin sisa elemen left
#         while i < len(lefthalf):
#             x[k] = lefthalf[i]
#             i = i + 1
#             k = k + 1

#         # salin sisa elemen right
#         while j < len(righthalf):
#             x[k]= righthalf[j]
#             j= j + 1
#             k= k + 1
#             print("Merging ", x)
# x = [22, 10, 15, 3, 8, 2]
# margeSort(x)
# print(x)

# # BINARY SEARCH 
# def BinSearch(data, key):
#     awal = 1
#     akhir = len(data) + 1
#     ketemu = False
#     while ( awal <= akhir ) and not ketemu:
#         tengah = int((awal + akhir)/2)
#         if key == data[tengah]:
#             ketemu = True
#             print("data", key, "ditemukan diposisi", tengah+1)
#         elif key < data[tengah]:
#             akhir = tengah - 1
#         else:
#             awal = tengah + 1
#     if not ketemu:
#         print("data tidak ditemukan")

# data = [1, 3, 9, 11, 15, 22,29, 31, 48]
# BinSearch(data, 9  )

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

data = [25, 20, 15, 3, 7, 2, 1]
merge_sort(data)
print("Hasil Merge Sort:", data)
