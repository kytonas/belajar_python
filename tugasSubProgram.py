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
pilihan = str(input('Pilih [1 : lingkaran, 2 : bujur sangkar, 3 : persegi panjang, 4 : segitiga] : '))
print('-' * 40)
if pilihan == "1" :
    jariJari = int(input('Masukkan jari-jari lingkaran : '))
    print('-' * 40)
    print(f'Luas lingkaran = {luasLingkaran(jariJari)}')
    print(f'Keliling lingkaran = {kelilingLingkaran(jariJari)}')
elif pilihan == "2" :
    sisiBujurSangkar = int(input('Masukkan sisi bujur sangkar : '))
    print('-' * 40)
    print(f'Luas bujur sangkar = {luasBujurSangkar(sisiBujurSangkar)}')
    print(f'Keliling bujur sangkar = {kelilingBujurSangkar(sisiBujurSangkar)}')
elif pilihan == "3" :
    panjangPersegiPanjang = int(input('Masukkan panjang persegi panjang : '))
    lebarPersegiPanjang = int(input('Masukkan lebar persegi panjang : '))
    print('-' * 40)
    print(f'Luas Persegi Panjang = {luasPersegiPanjang(panjangPersegiPanjang, lebarPersegiPanjang)}')
    print(f'Keliling Persegi Panjang = {kelilingPersegiPanjang(panjangPersegiPanjang, lebarPersegiPanjang)}')
elif pilihan == "4" :
    alasSegitiga = int(input('Masukkan alas segitiga : '))
    tinggiSegitiga = int(input('Masukkan tinggi segitiga : '))
    sisi1Segitiga = int(input('Masukkan sisi 1 segitiga : '))
    sisi2Segitiga = int(input('Masukkan sisi 2 segitiga : '))
    sisi3Segitiga = int(input('Masukkan sisi 3 segitiga : '))
    print('-' * 40)
    print(f'Luas segitiga = {luasSegitiga(alasSegitiga, tinggiSegitiga)}')
    print(f'Keliling segitiga = {kelilingSegitiga(sisi1Segitiga, sisi2Segitiga, sisi3Segitiga)}')
else :
    print('Pilihan tidak tersedia')