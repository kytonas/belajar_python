# import my_module as m

# print(f'PI = {m.PI}')
# print(f'Luas Lingkaran = {m.luasLingkaran(10)}')
# print(f'Keliling Lingkaran = {m.kelilingLingkaran(10)}')
# print(f'Tahun 2000 adalah Kabisat ? : {m.kabisat(2000)}')

from my_module import PI, luasLingkaran
print(f'PI = {PI}')
print(f'Luas Lingkaran = {luasLingkaran(10)}')

# from my_module import * # Tidak direkomendasikan
# print(f'PI = {PI}')
# print(f'Luas Lingkaran = {luasLingkaran(10)}')
