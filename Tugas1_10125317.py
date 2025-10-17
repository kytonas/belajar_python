# 1). Algoritma konversi durasi waktu
# {I.S : User input satuan detik}
# {F.S : Menampilkan hasil hari, jam, menit, detik}
# Kamus/Deklarasi :
# Detik, Menit, Jam, Hari, S_Hari, S_Menit, S_jam : integer
# Algoritma :
print("Konversi alamat durasi waktu")
print("="*40)
Detik = int(input('Masukkan detik = '))
Hari = Detik // 86400
S_Hari = Detik % 86400
Jam = S_Hari // 3600
S_Jam = S_Hari % 3600
Menit = S_Jam // 60
S_Menit = S_Jam % 60
hasilDetik = S_Menit
print(f'{Detik} detik = {Hari} hari, {Jam} jam, {Menit} menit, {hasilDetik} detik')

# 2). Algoritma konversi waktu proyek yang dikerjakan
# {I.S : User input Hari}
# {F.S : Menampilkan hasil Tahun, Bulan, Hari}
# Kamus/Deklarasi :
# Tahun, S_Tahun, Bulan, S_Bulan, Hari, total_Hari : integer
print("Total waktu proyek yang dikerjakan")
print("="*40)
Hari = int(input('Masukkan Hari = '))
Tahun = Hari // 365
S_Tahun = Hari % 365
Bulan = S_Tahun // 30
S_Bulan = S_Tahun % 30
total_Hari = S_Bulan
print(f'{Hari} Hari = {Tahun} Tahun, {Bulan} Bulan, {total_Hari} Hari')

# 3). Algoritma berat badan ideal
# {I.S : User input tinggi badan}
# {F.S : Menampilkan hasil berat badan ideal}
# Kamus/Deklarasi :
# tinggi_badan : integer
# berat_badan_ideal : float
# Algoritma :
tinggi_badan = int(input('Masukkan tinggi badan = '))
beratBadanIdeal = tinggi_badan - 100 - (0.1 * (tinggi_badan - 100))
print(f'Berat badan ideal = {beratBadanIdeal}')