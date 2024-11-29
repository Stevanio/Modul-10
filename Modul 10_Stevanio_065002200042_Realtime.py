def binary_search(data_list, low, high, x):
    if high >= low:
        index_mid = (high + low) // 2
        if data_list[index_mid] == x:
            return index_mid
        elif data_list[index_mid] > x:
            return binary_search(data_list, low, index_mid - 1, x)
        else:
            return binary_search(data_list, index_mid + 1, high, x)
    else:
        return -1
data_list = [1,8,7,26,10,13,14,15,3,4,5,9]
print(f'List data sebelum disort = {data_list}')
x = int(input("masukkan angka yang dicari: "))
data_list.sort()
print(f'List data sesudah disort = {data_list}')


hasil = binary_search(data_list, 0, len(data_list)-1, x) + 1
 
if hasil > 1:
    print(f'Element ditemukan pada posisi ke {hasil}')
else:
    print('Element tidak ditemukan pada list')
