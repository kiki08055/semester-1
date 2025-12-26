def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
    return max_value, fractions
n = int(input('Masukkan Jumlah Barang: '))
value = input('Masukkan Nilai Dari {} barang yang anda input: '
        .format(n)).split()
value = [int(v) for v in value]
weight = input('Masukkan data berat {} barang yang anda input: '
    .format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Input Berat Maksimal: '))
max_value, fractions = fractional_knapsack(value, weight, capacity)
print('Nilai Maksimal barang yang bisa di bawa:', max_value)
print('Nilai barang yang harus di ambil:', fractions)