print('Program menghitung nilai')
print('-'*30)

nilaiTugas = int(input('Nilai Tugas : '))
nilaiUts = int(input('Nilai UTS : '))
nilaiUas = int(input('Nilai UAS : '))

hasilAkhir = 0.3 * nilaiTugas + 0.3 * nilaiUts + 0.4 * nilaiUas
print(f'Nilai Akhir : {hasilAkhir}')

if hasilAkhir >= 80 and hasilAkhir <= 100 :
    print('Indeks Mutu : A')
    print('Keterangan : Sangat Baik')
elif hasilAkhir >= 68 and hasilAkhir < 80 :
    print('Indeks Mutu : B')
    print('Keterangan : Baik')
elif hasilAkhir >= 56 and hasilAkhir < 68 :
    print('Indeks Mutu : C')
    print('Keterangan : Cukup')
elif hasilAkhir >= 40 and hasilAkhir < 56 :
    print('Indeks Mutu : D')
    print('Keterangan : Kurang')
else :
    print('Indeks Mutu : E')
    print('Keterangan : Sangat Kurang')