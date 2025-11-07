# for i in range(1,6) : #for to do
#     print(i)
# print('')
# for i in range(5,0,-1) : #for downto do
#     print(i)
# print('')
# i = 0
# while i <= 10 : #while do
#     print(i)
#     # i = i + 2.5 
#     i += 2.5
# print('')
# lagi = 'Y'
# total = 0
# i = 0
# while lagi.upper() == 'Y' :
#     i = int(input('Input Angka : '))
#     # total = total + i
#     total += i
#     print(f"Total Sekarang : {total}")
#     lagi = str(input('Lagi ? '))
print('')
saldoAwal = float(input('Saldo Awal  : Rp. '))
bunga = float(input('Bunga (%) : '))
jangkaWaktu = int(input('Jangka Waktu : '))
# saldoAkhir = saldoAwal

# for i in range(1, jangkaWaktu + 1) :
#     # saldoAkhir = saldoAkhir + saldoAkhir * bunga / 100
#     saldoAwal = saldoAwal + saldoAwal * bunga / 100
#     # print(f'Saldo akhir bulan ke-{i} = {saldoAkhir}')
#     print(f'Saldo akhir bulan ke-{i} = {saldoAwal}')

i = 1
while i <= jangkaWaktu :
    saldoAwal = saldoAwal + saldoAwal * bunga / 100
    print(f'Saldo akhir bulan ke-{i} = {saldoAwal}')
    i += 1