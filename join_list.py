L1 = [10, 20, 30, 40]
L2 = ['one', 'two', 'three', 'four']

for i in L2:
    L1.append(i)

print(f'Joined list: {L1}')

# Membuat dua list yang akan digabungkan
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Menggunakan metode extend() untuk menggabungkan list
list1.extend(list2)
print(f'Hasil penggabungan list: {list1}')
