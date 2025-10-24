# program biaya rental warnet
inputJamMasuk = int(input('Jam Masuk : '))
inputMenitMasuk = int(input('Menit Masuk : '))
inputJamKeluar = int(input('Jam Keluar : '))
inputMenitKeluar = int(input('Menit Keluar : '))
print('-'*40)

masuk = inputJamMasuk * 60
totalMasuk = masuk + inputMenitMasuk
keluar = inputJamKeluar * 60
totalKeluar = keluar + inputMenitKeluar
selisih = totalKeluar - totalMasuk

konversiJam = selisih // 60
konversiMenit = selisih % 60
hargaRental = selisih * 5000
print(f'Lama Rental  : {selisih} Menit ({konversiJam} Jam {konversiMenit} Menit)')
print(f'Biaya Rental : Rp. {hargaRental}')
