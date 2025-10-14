# #contoh operasi aritmatika
# a = 15
# b = 7
# print('Aritmatika')
# print('a + b = ',a+b)
# print('a - b = ',a-b)
# print('a * b = ',a*b)
# print('a / b = ',a/b)
# print('a // b = ',a//b) #div
# print('a % b = ',a%b) #mod
# print('a ** b = ',a**3) #pangkat
# # Contoh operasi perbandingan
# print('Perbandingan')
# print('a == b = ', a == b)
# print('a > b = ', a > b )
# print('a < b = ', a < b )
# print('a >= b = ', a >= b )
# print('a <= b = ', a <= b )
# print('a != b = ', a != b ) # tidak sama dengan

# # TIPE DATA STRING
# nama = 'Bandung Kota kembang'
# print(nama)
# nama = "Bandung Kota Kembang"
# print(nama)
# nama = '''Bandung
# Kota
# Kembang'''
# print(nama)
# nama = 'Bandung '\
# 'Kota '\
# 'Kembang'
# print(nama)
# # Operasi penggabungan (concate)
# print("hello " + "world")
# print('2'+'5')
# print("James"+" "+ "Bond")
# print("ha"*3)
# print("-"*10)
# # Contoh String Method
# s = 'Python OK'
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.replace('OK', 'Bagus'))
# print(s.find('on'))
# # Mengakses elemen string berdasarkan posisi
# print(s[0])
# print(s[5])
# print(s[-1])
# print('Algoritma'[2])

# TIPE DATA LOGIK (BOOLEAN)
# a = True
# b = False
# print('a = ',a)
# print('b = ',b)
# print('a and b = ',a and b)
# print('a or b = ',a or b)
# print('a xor b = ',a ^ b)
# print('not a = ',not a)

# Program menjumlah Dua buah Angka (Dengan inputan Langsung)
# {I.S : Dimasukkan 2 buah nilai ke dalam var angka1 dan angka2}
# {F.S : Menampilkan hasil penjumlahan angka1 dan angka2}
# print('Program menjumlah Dua buah Angka (Dengan inputan Langsung)')
# print('-'*60)
# angka1 = 10
# angka2 = 20
# hasil = angka1 + angka2
# print('Angka ke-1 = ',angka1)
# print('Angka ke-2 = ',angka2)
# print('Hasil = ',hasil)
# print(f'Hasil = {angka1} + {angka2} = {hasil}')

# Program menjumlah Dua buah Angka (Dengan inputan Tidak Langsung)
# {I.S : User memasukkan 2 buah nilai ke dalam var angka1 dan angka2}
# {F.S : Menampilkan hasil penjumlahan angka1 dan angka2}
print('Program menjumlah Dua buah Angka (Dengan inputan Tidak Langsung)')
print('-'*65)
angka1 = int(input('Masukkan angka ke-1 : '))
angka2 = int(input('Masukkan angka ke-2 : '))
hasil = angka1 + angka2
print(f'Hasil = {hasil}')