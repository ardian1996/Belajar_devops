# Soal 1: Perbedaan Data Structure
'''
- List: Tipe data terurut yang bisa diubah (mutable), memungkinkan elemen duplikat. Diakses dengan indeks.
- Tuple: Tipe data terurut yang tidak bisa diubah (immutable), memungkinkan elemen duplikat. Diakses dengan indeks.
- Set: Tipe data tidak terurut yang tidak memungkinkan elemen duplikat. Tidak diakses dengan indeks.
- Dictionary: Tipe data tidak terurut yang menyimpan pasangan key-value. Key harus unik.
'''

#------------------------------------------------------------------
# Soal 2: Akses List
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
# slicing dari indeks 1 sampai sebelum indeks 5
print(a[1:5])

# Expected Output : ['13b', 'aa1', 1.32, 22.1]

#-------------------------------------------------------------------
# Soal 3: Akses Nested List
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# akses elemen dari list di indeks 1, dan ambil elemen ke-0 dan ke-2
print([a[1][0], a[1][2]])

# Expected Output : [0, 6]

#---------------------------------------------------------------------
# Soal 4: List Manipulation
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# ubah nilai a[0][2] menjadi 10 dan a[1][0] menjadi 11
a[0][2] = 10
a[1][0] = 11
print(a)

# Expected Output : [[5, 9, 10], [11, 0, 6]]

#---------------------------------------------------------------------
# Soal 5: Delete Element List
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# menggunakan remove untuk menghapus elemen
areas.remove("bathroom")
areas.remove(10.50)

print(areas)

# Expected Output: ['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'poolhouse', 24.5, 'garage', 15.45]

#-----------------------------------------------------------------------------------
# Soal 6: List Comprehension
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# mencari elemen yang habis dibagi 2
T = [x for x in S if x % 2 == 0]

print(T)

# Expected Output: [0, 4, 16, 36, 64]

#----------------------------------------------------------------------------------
# Soal 7: Mengakses Tuple
tuple_1 = (1, 2, 6, 7, 8, 9, 10)

# akses tuple dengan slicing dari indeks 2 sampai sebelum 5
print(tuple_1[2:5])

# Expected Output: (6, 7, 8)

#-------------------------------------------------------------------------------
# Soal 8: Menambahkan key-value baru ke Dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}

# menambahkan key 'italy' dengan value 'rome'
europe['italy'] = 'rome'

# cek apakah key 'italy' ada dalam dictionary
print('italy' in europe)

# Expected Output: True

#--------------------------------------------------------------------------------
# Soal 9: Update dan Remove Dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# update ibukota germany menjadi berlin
europe['germany'] = 'berlin'

# hapus key 'australia'
del europe['australia']

print(europe)

# Expected Output: {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw'}

#-----------------------------------------------------------------------------------
# Soal 10: Nested Dictionary
country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

# akses populasi germany
print(country['germany']['population'])

# update negara indonesia
country['indonesia'] = {'capital': 'jakarta', 'population': 250}

print(country)

# Expected Output:
# 80.62
# {'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'indonesia': {'capital': 'jakarta', 'population': 250}}

#------------------------------------------------------------------------------------
# Soal 11: Loop Dictionary
country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }

# loop untuk menampilkan ibukota
for country_name, country_info in country.items():
    print('Ibukota ' + country_name + ' adalah ' + country_info['capital'])

# Expected Output:
# Ibukota spain adalah madrid
# Ibukota france adalah paris
# Ibukota germany adalah berlin
# Ibukota norway adalah oslo
# Ibukota indonesia adalah jakarta

#------------------------------------------------------------------------------ 
# Soal 12: Remove Duplicate using set
obj_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]

# menggunakan set untuk menghilangkan duplikat
obj_set = set(obj_list)

print(obj_set)

# Expected Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#---------------------------------------------------------------------------------
# Soal 13: Mengubah dan menghapus anggota set
set_1 = {1, 2, 3, 4, 5}

# tambahkan {6, 7, 8}
set_1.update({6, 7, 8})

# hapus nilai 8
set_1.remove(8)

print(set_1)

# Expected Output: {1, 2, 3, 4, 5, 6, 7}

#----------------------------------------------------------------------------------
# Soal 14: Operasi pada Set
set_2 = {6, 8, 9, 10, 24}
set_3 = {6, 10, 8, 25, 13}

# mencari irisan set
set_intersection = set_2.intersection(set_3)

print(set_intersection)

# Expected Output: {6, 8, 10}
