# Algoritma : menghitung komisi
# {I.S : Masukkan 2 input ke dalam dua variabel}
# {F.S : Menampilkan hasil komisi}
nama = str(input('Masukkan nama salesman : '))
nilaiPenjualan = int(input('Masukkan nilai penjualan : '))
hasil = 5 * nilaiPenjualan / 100
print(f'Komisi penjualan milik {nama}adalah {hasil}')