#array 2 dimensi
# M = [[1,2],[3,4]] #Array atau matriks 'M' berukuran 2x2
# print(M[0][0])
# print(M[0][1])
# print(M[1][0])
# print(M[1][1])
# for i in M :
#     print(i)

Nbar = 3
Nkol = 3
M1 = [] #Membuat Array M1
M2 = [] #Membuat Array M2
M3 = []
M4 = []
M5 = []

def isiMatriks(A):
    for i in range(0,Nbar) :
        kol = []
        for j in range (0, Nkol) :
            elemen = int(input(f'Masukkan elemen array baris ke-{i+1} kolom-{j+1} : '))
            kol.append(elemen)
        A.append(kol)

def tampilMatriks(A):
    # for i in range(0,Nbar) :
    #     for j in range(0,Nkol) :
    #         print(f'Elemen array baris-{i+1} kolom-{j+1} : {A[i][j]}')
    # print('')
    for i in A :
        print(i)

def penjumlahanMatriks(A,A1,A2):
    for i in range(0,Nbar) :
        kol = []
        for j in range (0, Nkol) :
            elemen = A1[i][j] + A2[i][j]
            kol.append(elemen)
        A.append(kol)

def penguranganMatriks(A,A1,A2):
    for i in range(0,Nbar) :
        kol = []
        for j in range (0, Nkol) :
            elemen = A1[i][j] - A2[i][j]
            kol.append(elemen)
        A.append(kol)

def perkalianMatriks(A,A1,A2):
    for i in range(0,Nbar) :
        kol = []
        for j in range (0, Nkol) :
            elemen = 0
            for k in range (0, Nbar) :
                elemen = elemen + (A1[i][k] * A2[k][j])
            kol.append(elemen)
        A.append(kol)




print("Pengisian Elemen Array 2D ke-1: ")
print('-'*40)
isiMatriks(M1)
print("Pembacaan Elemen Array 2D ke-1: ")
print('-'*40)
tampilMatriks(M1)
print('')
print("Pengisian Elemen Array 2D ke-2: ")
print('-'*40)
isiMatriks(M2)
print("Pembacaan Elemen Array 2D ke-2: ")
print('-'*40)
tampilMatriks(M2)
print('')
print("Penjumlahan Elemen Array 2D : ")
print('-'*40)
penjumlahanMatriks(M3,M1,M2)
tampilMatriks(M3)
print('')
print("Pengurangan Elemen Array 2D : ")
print('-'*40)
penguranganMatriks(M4,M1,M2)
tampilMatriks(M4)
print('')
print("Perkalian Elemen Array 2D : ")
print('-'*40)
perkalianMatriks(M5,M1,M2)
tampilMatriks(M5)



