print('Program validitas tanggal')
print('-'*30)

tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan : '))
tahun = int(input('Tahun : '))

if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12 :
    if tanggal > 31 :
        print(f'Tanggal {tanggal}/{bulan}/{tahun} adalah tanggal valid')
    else :
        print(f'Tanggal {tanggal}/{bulan}/{tahun} bukan tanggal valid')
elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11 :
    if tanggal > 30 :
        print(f'Tanggal {tanggal}/{bulan}/{tahun} adalah tanggal valid')
    else :
        print(f'Tanggal {tanggal}/{bulan}/{tahun} bukan tanggal valid')
else : 
    if tanggal > 29 :
        print(f'Tanggal {tanggal}/{bulan}/{tahun} adalah tanggal valid')
    else :
        print(f'Tanggal {tanggal}/{bulan}/{tahun} bukan tanggal valid')