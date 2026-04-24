# Class node (digunakan untuk membuat node baru)
class Node : 
    def __init__(self,info):
        self.info = info
        self.next = None

# Class single linked list (digunakan untuk membuat linked list)
class LinkedList : 
    def __init__(self):
        self.awal = None

    # Operasi Traversal (method Traversal)
    def traversal(self):
        if self.awal is None: #kondisi LL kosong
            print('Linked list kosong')
        else: #Kondisi LL memiliki elemen
            n = self.awal
            while n is not None:
                print(n.info, end=' -> ')
                n = n.next

    # Method menghitung jumlah elemen
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

    # Operasi penambahan elemen
    # Penambahan di posisi awal (Method Tambah Awal)
    def tambah_awal(self,info):
        node_baru = Node(info)
        if self.awal is None: #kondisi LL kosong
            self.awal = node_baru
        else : #kondisi ll memiliki elemen
            node_baru.next = self.awal
            self.awal = node_baru

    def tambah_akhir(self, info):
        node_baru = Node(info)
        if self.awal is None:
            self.awal = node_baru
        else : 
            n = self.awal
            while n.next is not None:
                n = n.next
            n.next = node_baru
    
    # Penambahan di posisi tengah (method tambah tengah)
    def tambah_tengah(self, info, posisi):
        j_elemen = self.jumlah_elemen()
        node_baru = Node(info)
        if self.awal is None or posisi <= 1: #kondisi LL kosong atau posisi sisip <= 1
            self.tambah_awal(info)
        else: #Kondisi LL memiliki elemen
            if posisi > j_elemen: #Kondisi posisi sisip di luar jangkauan LL
                self.tambah_akhir(info)
            else: #Kondisi posisi sisip berada dalam jangkauan LL
                pos = 1
                n = self.awal
                while pos < posisi-1:
                    pos += 1
                    n = n.next
                node_baru.next = n.next
                n.next = node_baru

ll = LinkedList()
ll.tambah_awal(10)
ll.tambah_awal(5)
ll.tambah_akhir(2)
ll.tambah_akhir(8)
ll.tambah_tengah(8, 3)
ll.tambah_tengah(5, 2)
ll.traversal()
print('')
# print(ll.jumlah_elemen())