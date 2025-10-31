# print('Program Penentuan Hadiah')
# print('-'*30)
# ranking = int(input('Ranking : '))
# rataRata = float(input('Rata-rata : '))

# if ranking == 1 and rataRata > 8 :
#     print('Anak mendapatkan hadiah')
# else : 
#     print('Anak tidak mendapatkan hadiah')



# print("Program menentukan kuadran")
# print('-'*30)
# x = float(input('Nilai x : '))
# y = float(input('Nilai y : '))

# if x > 0 and y > 0 :
#     posisi = 'Kuadran I'
# elif x < 0 and y > 0 :
#     posisi = 'Kuadran II'
# elif x < 0 and y < 0 :
#     posisi = 'Kuadran III'
# elif x > 0 and y < 0 :
#     posisi = 'Kuadran IV'
# elif x == 0 and y == 0 :
#     posisi = 'Titik Pusat'
# elif x != 0 and y == 0 :
#     posisi = 'Pusat Sumbu X'
# elif x == 0 and y != 0 :
#     posisi = 'Pusat Sumbu Y'
# print(f'Koordinat ({x},{y}) berada pada {posisi}')

# print('Program umur dewasa atau anak-anak')
# print('-'*30)

# umur = int(input('Umur : '))
# if umur >= 17 :
#     print('Dewasa')
# else : 
#     print('Anak-anak')

# umur = int(input('Umur : '))
# dewasa = umur >= 17

# if not dewasa :
#     print('Anak-anak')
# else :
#     print('Dewasa')

print('Program penentuan keikutsertaan pemilu')
print('-' * 35)

umur = int(input('Umur : '))
if umur >= 17 :
    print('Anda Boleh ikut pemilu')
else :
    status = str(input('Status Menikah [Y/T] : '))
    if status.upper() == 'Y' :
        print('Anda Boleh ikut pemilu')
    elif status.upper() == 'T' : 
        print('Anda belum boleh ikut pemilu')
    else :
        print('Input tidak diketahui')