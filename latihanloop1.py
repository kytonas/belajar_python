# Program setor dan tarik tunai

transaksiLagi = 'Y'
saldo = 10000

while transaksiLagi.upper() == 'Y' :
    kodeTransaksi = int(input('Kode Transaksi [0/1] : '))
    jumlahUang = float(input('Jumlah Uang : Rp. '))
    if kodeTransaksi == 0 :
        saldo = saldo + jumlahUang
        print(f'Saldo Saat ini : {saldo}')
    elif kodeTransaksi == 1 :
        if saldo - jumlahUang >= 10000 :
            saldo = saldo - jumlahUang
            print(f'Saldo Saat ini : {saldo}')
        else :
            print('Saldo tidak mencukupi')
    transaksiLagi = str(input("Transaksi lagi [Y/T] ? "))