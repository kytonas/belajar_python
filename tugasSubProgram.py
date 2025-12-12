#Program perhitungan luas dan keliling

#lingkaran (function)
def luasLingkaran(radius) :
    return 22 / 7 * radius ** 2

def kelilingLingkaran(radius) :
    return 2 * 22 / 7 * radius

#bujur sangkar (function)
def luasBujurSangkar(sisi) :
    return sisi ** 2

def kelilingBujurSangkar(sisi) :
    return 4 * sisi

#persegi panjang (function)
def luasPersegiPanjang(panjang, lebar) :
    return panjang * lebar

def kelilingPersegiPanjang(panjang, lebar) :
    return 2 * (panjang + lebar)

#segitiga (function)
def luasSegitiga(alas, tinggi) :
    return 1/2 * alas * tinggi

def kelilingSegitiga(sisi1, sisi2, sisi3) :
    return sisi1 + sisi2 + sisi3


#Program Utama
print('Aplikasi Perhitungan Luas dan Keliling')
print('-' * 40)
print('''
        1. Lingkaran
        2. Bujur Sangkar
        3. Persegi Panjang
        4. Segitiga
        0. Keluar
    ''')
print('-' * 40)
pilihan = str(input('Pilihan anda ? '))
print('-' * 40)
if pilihan == "1" :
    print('Perhitungan luas dan keliling Lingkaran')
    print('-' * 40)
    jariJari = int(input('Radius : '))
    print(f'Luas lingkaran = {luasLingkaran(jariJari)}')
    print(f'Keliling lingkaran = {kelilingLingkaran(jariJari)}')
elif pilihan == "2" :
    print('Perhitungan luas dan keliling Bujur Sangkar')
    print('-' * 40)
    sisiBujurSangkar = int(input('Sisi : '))
    print(f'Luas bujur sangkar = {luasBujurSangkar(sisiBujurSangkar)}')
    print(f'Keliling bujur sangkar = {kelilingBujurSangkar(sisiBujurSangkar)}')
elif pilihan == "3" :
    print('Perhitungan luas dan keliling Persegi Panjang')
    print('-' * 40)
    panjangPersegiPanjang = int(input('Panjang : '))
    lebarPersegiPanjang = int(input('Lebar : '))
    print(f'Luas Persegi Panjang = {luasPersegiPanjang(panjangPersegiPanjang, lebarPersegiPanjang)}')
    print(f'Keliling Persegi Panjang = {kelilingPersegiPanjang(panjangPersegiPanjang, lebarPersegiPanjang)}')
elif pilihan == "4" :
    print('Perhitungan luas dan keliling Segitiga')
    print('-' * 40)
    alasSegitiga = int(input('Alas : '))
    tinggiSegitiga = int(input('Tinggi : '))
    sisi1Segitiga = int(input('Sisi 1 : '))
    sisi2Segitiga = int(input('Sisi 2 : '))
    sisi3Segitiga = int(input('Sisi 3 : '))
    print(f'Luas segitiga = {luasSegitiga(alasSegitiga, tinggiSegitiga)}')
    print(f'Keliling segitiga = {kelilingSegitiga(sisi1Segitiga, sisi2Segitiga, sisi3Segitiga)}')
else :
    print('Pilihan tidak tersedia')