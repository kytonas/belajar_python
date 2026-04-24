class Node :
    def __init__(self, info):
        self.info = info
        self.next = None

# Operasi Penambahan
# a). Tambah di posisi akhir
class LinkedList :
    def __init__(self):
        self.awal = None

    def traversal(self):
        if self.awal is None: #kondisi LL kosong
            print('Linked list kosong')
        else: #Kondisi LL memiliki elemen
            n = self.awal
            while n is not None:
                print(n.info, end=' -> ')
                n = n.next

    def jumlah_elemen(self):
        if self.awal is None: #Kondisi LL kosong
            return 0
        else: #Kondisi LL memiliki elemen
            jumlah = 0
            n = self.awal
            while n.next is not None:
                jumlah += 1
                n = n.next
            jumlah += 1
            return jumlah

    def tambah_akhir(self, info):
        node_baru = Node(info)
        if self.awal is None:
            self.awal = node_baru
        else : 
            n = self.awal
            while n.next is not None:
                n = n.next
            n.next = node_baru
            node_baru.prev = n
    
# b). Tambah di posisi tengah
    def tambah_tengah(self, info, posisi):
        j_elemen = self.jumlah_elemen()
        node_baru = Node(info)
        if posisi > j_elemen :
            self.tambah_akhir(info)
        else :
            pos = 1
            n = self.awal
            while pos < posisi :
                pos += 1
                n = n.next
            m = n.prev
            m.next = node_baru
            node_baru.prev = m
            node_baru.next = n
            n.prev = node_baru
   
# Operasi penghapusan
# a). Hapus di posisi awal
    def hapus_awal(self):
        if self.awal is None :
            print('Tidak bisa menghapus elemen')
        elif self.awal.next is None :
            self.awal = None
        else :
            self.awal = self.awal.next
            self.awal.prev = None
        
# b). Hapus di posisi akhir 
    def hapus_akhir(self):
        if self.awal is None :
            print('Tidak bisa menghapus elemen')
        elif self.awal.next is None:
            self.awal = None
        else :
            n = self.awal
            while n.next.next is not None:
                n = n.next
            n.next = None

# c). Hapus di posisi tengah
    def hapus_tengah(self, posisi):
        j_elemen = self.jumlah_elemen()
        if self.awal is None:
            print("Tidak bisa menghapus elemen")
        else:
            pos = 1
            n = self.awal
            while pos < posisi :
                pos += 1
                n = n.next
            n2 = n.prev
            n3 = n.next
            n2.next = n3
            n3.prev = n2
                
                

ll = LinkedList()
ll.tambah_akhir(4)
ll.tambah_akhir(1)
ll.tambah_akhir(1)
ll.tambah_akhir(5)
ll.tambah_tengah(5, 3)
ll.hapus_awal()
ll.hapus_akhir()
ll.hapus_tengah(2)
ll.traversal()
