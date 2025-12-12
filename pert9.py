# def jumlahDeret(N) : #function Jumlah deret
#     jumlah = 0
#     for i  in range (1, N+1) :
#         jumlah = jumlah + i
#     return jumlah

# def besarBunga(awal, persenBunga, waktu) :
#     return awal * (1 + persenBunga / 100) ** waktu

# # Program utama
# # jumlah = jumlahDeret(5)
# # print(f'Jumlah deret 1-5 : {jumlah}')
# # print(f'Jumlah deret 1-5 : {jumlahDeret(5)}')
# # print(f'Besar Bunga : {besarBunga(100000,3,5)}')
# # i_jumlah = int(input('Masukkan angka : '))
# # jumlah = jumlahDeret(i_jumlah)
# print(f'Jumlah deret : {jumlah}')

# def tampilGanjil(awal, akhir) : #Procedure Menampilkan ganjil
#     for i in range (awal, akhir+1):
#         if i % 2 != 0 :
#             print(i, end=' ')

# def tampilGenap(awal, akhir) : #Procedure Menampilkan genap
#     for i in range (awal, akhir+1):
#         if i % 2 == 0 :
#             print(i, end=' ')

# def totalGanjil(awal, akhir) : #procedure total ganjil
#     total = 0
#     for i in range (awal, akhir+1):
#         if i % 2 != 0 :
#             total = total + i
#     return total

# def totalGenap(awal, akhir) : #procedure total genap
#     total = 0
#     for i in range (awal, akhir+1):
#         if i % 2 == 0 :
#             total = total + i
#     return total

# # Program utama
# n_awal = int(input('Nilai Awal : '))
# n_akhir = int(input('Nilai Akhir : '))
# print('-'*35)
# print(f'Bilangan ganjil antara {n_awal} - {n_akhir}')
# tampilGanjil(n_awal,n_akhir)
# print('')
# print(f'Bilangan genap antara {n_awal} - {n_akhir}')
# tampilGenap(n_awal,n_akhir)
# print('')
# print(f'Total bilangan ganjil : {totalGanjil(n_awal, n_akhir)}')
# print(f'Total bilangan genap : {totalGenap(n_awal, n_akhir)}')

def faktorial(N) :
    if N <= 1 :
        return 1
    else :
        return N * faktorial(N-1)
    
def fibonacci(N) :
    if N <= 1 :
        return N
    else :
        return fibonacci(N-2) + fibonacci(N-1)
    
print(f'Faktorial 4 = {faktorial(4)}')
for i in range(0, 11) :
    print(fibonacci(i), end=" ")
