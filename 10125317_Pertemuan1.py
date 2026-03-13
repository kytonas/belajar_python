# # 1. LIST
list1 = [] #membuat list kosong
print(list1)
list1 = [3,2,1,4,5,3] 
print(list1)
# mengakses elemen
print(list1[1])
for i in list1 :
    print(i)
print('')
for i in range(0, len(list1)) :
    print(f'Elemen list1 indeks ke-{i} : {list1[i]}')
# menambah elemen
list1 = list1 + [7,8] # Menambah dengan concatenation
print(list1)
list1.append(9) # Menambah dengan append
print(list1)
list1.insert(1,10) #menambah dengan insert
print(list1)
list1.extend([11,12]) # menambah dengan extend
print(list1)
#mengupdate elemen
list1[1] = 13
print(list1)
#Menghapus elemen
list1.remove(3) #menghapus dengan remove
print(list1)
dihapus = list1.pop(0) #menghapus dengan pop
print(f'Elemen yang dihapus : {dihapus}')
print(list1)
del list1[0] #menghapus dengan del
print(list1)

# 2. TUPLE
t1 = () #membuat tuple kosong
print(t1)
t1 = (4,1,5,3,2,3,6)
print(t1)
#mengakses elemen
print(t1[1])
for i in t1 :
    print(i)
print("")
for i in range(0,len(t1)):
    print(f'Elemen t1 indeks ke-{i} : {t1[i]}')

# 3. SET
s1 = set({}) #membuat set kosong
print(type(s1))
s1 = {3,2,1,3,4,5}
print(s1)
#mengakses data
for i in s1:
    print(i)
#menambah elemen
s1.add(6) #menambah dengan add
print(s1)
s1.update([6,7,8]) #menambah dengan update
print(s1)
#menghapus elemen
s1.remove(8) #menghapus dengan remove
print(s1)
s1.discard(7) #menghapus dengan discard
print(s1)
dihapus = s1.pop() #menghapus dengan pop
print(f'Elemen yang dihapus : {dihapus}')
print(s1)
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(f'A: {A}')
print(f'B: {B}')
print(f'A union B = {A.union(B)}')
print(f'A intersection B = {A.intersection(B)}')
print(f'A diiference B = {A.difference(B)}')
print(f'B diiference A = {B.difference(A)}')
print(f'A Sym diiference B = {A.symmetric_difference(B)}')

# 4. DICTIONARY
mhs = {} #membuat dict kosong
print(mhs)
mhs = {'nama' : 'Asep', 'umur':20, 'kota' : 'Garut'}
print(mhs)
#mengakses elemen
print(mhs['nama'])
for key in mhs:
    print(f'{key} = {mhs[key]}')
print(f'kota: {mhs.get("kota")}' )
#menambah/mengubah elemen
mhs['nilai'] = 90 #menambah dengan kurung siku
print(mhs)
mhs['nilai'] = 100
print(mhs)
mhs.update({'nilai':80, 'kelas' : 'IF-1'})
print(mhs)
#menghapus elemen
dihapus = mhs.pop('kelas')
print(f'elemen yang dihapus : {dihapus}') #menghapus dengan pop
print(mhs)
del mhs['nilai'] #menghapus dengan del
print(mhs)

kelas = ({ 'nama' : "IF-1",
           'siswa' : [{'nim':'10119001','nama':'Asep'},
                      {'nim':'10119002','nama':'Budi'},
                      {'nim':'10119003','nama':'Cecep'}
                    ]
        },
          { 'nama' : "IF-2",
            'siswa' : [{'nim':'10119004','nama':'Dede'},
                       {'nim':'10119005','nama':'Erna'} ]
          }
        )
for k in kelas:
    print("Nama Kelas : ", k['nama'])
    print("Banyak Siswa : ", len(k['siswa']))
    print("Daftar Siswa : ")
    for s in k['siswa']:
        print(s["nim"], " - ", s["nama"])
        print("------------------------------")