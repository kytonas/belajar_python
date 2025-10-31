print('Program menentukan tahun kabisat')
print('-'*30)
tahun = int(input('Tahun : '))

if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0 :
    print(f'Tahun {tahun} adalah tahun kabisat')
else :
    print(f'Tahun {tahun} bukan tahun kabisat')