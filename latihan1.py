# Program perhitungan tiket kereta api
print("Perhitungan Tiket Kereta Api")
print('-'*40)

print('Jurusan : ')
print('1. Jakarta')
print('2. Yogyakarta')
print('3. Surabaya')

pilihJurusan = int(input('Pilihan Jurusan [1/2/3] : '))
banyakTiket = int(input('Banyak Tiket : '))

if pilihJurusan == 1 :
    hargaTiket = 150000
elif pilihJurusan == 2 :
    hargaTiket = 300000
elif pilihJurusan == 3 :
    hargaTiket = 400000
else :
    hargaTiket = 0

print("")
totalBayar = hargaTiket * banyakTiket
print(f'Harga Tiket   : Rp. {hargaTiket:10.0f}')
print(f'Banyak Tiket  : {banyakTiket}')
print(f'Total Bayar   : Rp. {totalBayar:10.0f}')
