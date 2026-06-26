# Class Node 
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

# Class Circular Single Linked List
class CircularSingleLinkedList:
    def __init__(self):
        self.awal = None

    # Jumlah elemen
    def jumlahElemen(self):
        if self.awal is None:
            return 0
        else:
            jumlah = 0
            n = self.awal
            while n.next is not self.awal:
                jumlah += 1
                n = n.next
            jumlah += 1
            return jumlah

    # Operasi Traversal
    def traversal(self):
        if self.awal is None: # kondisi LL kosong
            print('Linked list kosong')
        else: # kondisi LL memiliki elemen
            n = self.awal
            while n.next != self.awal:
                print(n.info, end=' -> ')
                n = n.next
            print(n.info, end=' -> ')

    # Operasi penambahan elemen
    # Posisi awal
    def tambahAwal(self, info):
        node_baru = Node(info)
        if self.awal is None: # Kondisi LL kosong
            self.awal = node_baru
            node_baru.next = self.awal
        else: # Kondisi LL memiliki elemen
            n = self.awal
            while n.next is not self.awal:
                n = n.next
            node_baru.next = self.awal
            self.awal = node_baru
            n.next = self.awal
    #  Posisi Akhir
    def tambahAkhir(self, info):
        node_baru = Node(info)
        if self.awal is None: # Kondisi LL kosong
            self.awal = node_baru
            node_baru.next = self.awal
        else: # Kondisi LL memiliki elemen
            n = self.awal
            while n.next is not self.awal:
                n = n.next
            n.next = node_baru
            node_baru.next = self.awal

    # Posisi Tengah
    def tambahTengah(self, info, posisi):
        node_baru = Node(info)
        j_elemen = self.jumlahElemen()
        if self.awal is None or posisi <= 1: # Kondisi LL kosong atau posisi sisip <= 1
            self.tambahAwal(info)
        else: # Kondisi LL memiliki elemen
            if posisi > j_elemen:
                self.tambahAkhir(info)
            else:
                pos = 1
                n = self.awal
                while pos < posisi-1:
                    pos += 1
                    n = n.next
                node_baru.next = n.next
                n.next = node_baru
        
    # Operasi penghapusan elemen
    def hapusAwal(self):
        if self.awal is None:
            print('Tidak Bisa Mengapus elemen')
        elif self.awal.next is self.awal:
            self.awal = None
        else:
            n = self.awal
            while n.next is not self.awal:
                n = n.next
            self.awal = self.awal.next
            n.next = self.awal

    # Posisi Akhir
    def hapusAkhir(self):
        if self.awal is None:
            print('Tidak Bisa Mengapus elemen')
        elif self.awal.next is self.awal:
            self.awal = None
        else:
            n = self.awal
            while n.next.next is not self.awal:
                n = n.next
            n.next = self.awal

    # Posisi Tengah
    def hapusTengah(self, posisi):
        j_elemen = self.jumlahElemen()
        if self.awal is None: # Kondisi LL kosong    
            print('Tidak bisa menghapus elemen')
        else: # Kondisi LL memiliki elemen
            if posisi < 1 or posisi > j_elemen:
                print('Tidak bisa menghapus elemen')
            else:
                if posisi == 1:
                    self.hapusAwal()
                elif posisi == j_elemen:
                    self.hapusAkhir()
                else:
                    pos = 1
                    n = self.awal
                    while pos < posisi-1:
                        pos += 1
                        n = n.next
                    n.next = n.next.next


csll = CircularSingleLinkedList()
csll.tambahAwal(5)
csll.tambahAwal(7)
csll.tambahAkhir(6)
csll.tambahAkhir(8)
csll.tambahTengah(9, 2)
csll.tambahTengah(10, 3)
# csll.hapusAwal()
# csll.hapusAkhir()
csll.hapusTengah(3)
csll.traversal()
# print('')
# print(csll.jumlahElemen())