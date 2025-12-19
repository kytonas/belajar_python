jumlahSiswa = int(input('Masukkan jumlah Siswa : '))

totalNilai = 0
NILAI = []
Nmaks = 50
if jumlahSiswa <= 50 :
    for i in range(0, jumlahSiswa) :
        data = int(input('Masukkan nilai = '))
        NILAI.append(data)
        totalNilai = totalNilai + data

    print('=' * 30)
    print('Daftar Nilai Siswa')
    for i in range(0, jumlahSiswa) :
        print(f'Nilai Siswa : {NILAI[i]}')

    rataRata = totalNilai / jumlahSiswa
    print(f"Rata-rata Nilai : {rataRata}")
else :
    print(f'Jumlah siswa melebihi {Nmaks}')