# Program perhitungan nilai akhir (contoh pemilihan dengan 1 alternatif)
# print('Program Perhitungan Nilai Akhir')
# print('-'*35)
# uts = float(input('Nilai UTS : '))
# uas = float(input('Nilai UAS : '))
# na = 0.4 * uts + 0.6 * uas
# print(f'Nilai Akhir : {na}')
# if na == 100 :
#     print('>>>Sempurna<<<')

# Program perhitungan penjualan barang (Contoh Pemilihan dengan 2 alternatif)
# print('Program perhitungan penjualan barang')
# print('-'*40)
# hargaSatuan = float(input('Harga Satuan : '))
# qty = int(input('Quantity : '))
# subTotal = hargaSatuan * qty
# if qty >= 12 :
#     diskon = 0.2 * subTotal
# else :
#     diskon = 0
# totalBayar = subTotal - diskon
# print(f'Sub Total   : Rp. {subTotal:10.2f}')
# print(f'Diskon      : Rp. {diskon:10.2f}')
# print(f'Total Bayar : Rp. {totalBayar:10.2f}')

# Program keteranga warna lampu lalu lintas (Contoh pemilihan dengan lebih dari 2 alternatif)
print('Program keterangan warna lampu lalu lintas')
print('-'*40)
warna = str(input('Warna Lampu : '))
if warna.lower() == "hijau" :
    print('Silahkan Jalan')
elif warna.lower() == "kuning" :
    print('siap-siap/hati-hati')
elif warna.lower() == "merah" :
    print('Berhenti')
else :
    print('Warna tidak dikenal')