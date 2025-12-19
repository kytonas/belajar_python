# nama = ['maya', 'vino', 'ghina','vina']
# print(nama[1])
# print('')
# for i in nama: #cara pertama
#     print(i)
# print('')
# for i in range(0,len(nama)) : #cara ketiga dan len adalah tidak usah diitung
#     print(nama[i])

# A = [1,3,5,7,9] #membuat array A
# print(A[2]) #mengakses elemen array A ke-2
# print('')
# for i in range(len(A)): #mengakses elemen semua array A
#     print(f'Elemen array indeks ke-{i}: {A[i]}')

# Nmaks = 5
# A = [] #membuat array A
# print('Pengisian Elemen Array')
# print('-'*30)
# for i in range(0, Nmaks):
#     data = int(input(f'Masukkan array indeks ke-{i} : '))
#     A.append(data) #memasukkan data inputan ke dalam array A
# print('')
# print('Pembacaan elemen array')
# print('-' * 30)
# for i in range(0, Nmaks) :
#     print(f'Elemen array indeks ke-{i} : {A[i]}')

# nilai = []
nilaiKelas1 = []
nilaiKelas2 = []

def inputNilai(A,jml_siswa) :
    for i in range(0, jml_siswa):
        data = int(input(f'Masukkan nilai siswa ke-{i} : '))
        A.append(data)

def tampilNilai(A,jml_siswa):
    for i in range(0, jml_siswa):
        print(f'Nilai siswa ke-{i} : {A[i]}')

def hitungRataRata(A,jml_siswa) :
    total = 0
    for i in range(0, jml_siswa) :
        total =  total + A[i]
    rataRata = total / jml_siswa
    return rataRata

# program utama
jumlahKelas1 = int(input('Masukkan jumlah siswa Kelas ke-1 : '))
print('Pengisian data nilai kelas ke-1')
print('-' * 30)
inputNilai(nilaiKelas1, jumlahKelas1)
print('')
print('Data Nilai kelas ke-2')
print('-' * 30)
tampilNilai(nilaiKelas1, jumlahKelas1)
print(f'Rata-rata : {hitungRataRata(nilaiKelas1, jumlahKelas1)}')


jumlahKelas2 = int(input('Masukkan jumlah siswa Kelas ke-2 : '))
print('Pengisian data nilai kelas ke-2')
print('-' * 30)
inputNilai(nilaiKelas2, jumlahKelas2)
print('')
print('Data Nilai kelas ke-2')
print('-' * 30)
tampilNilai(nilaiKelas2, jumlahKelas2)
print(f'Rata-rata : {hitungRataRata(nilaiKelas2, jumlahKelas2)}')