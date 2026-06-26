# # Implemetasi Queue Menggunakan Struktur Data list
# q = [] #Membuat queue kosong
# print(q)
# q.append(10) #enqueue(10)
# q.append(20) #enqueue(20)
# q.append(15) #enqueue(15)
# print(q)
# dihapus = q.pop(0) #deque
# print(f'Elemen yang dihapus: {dihapus}')
# print(q)
# isEmpty = len(q)==0
# print(f'Queue kosong? {isEmpty}')
# print(f'Elemen front : {q[0]}')
# print(f'Elemen rear : {q[-1]}')

# # Implementasi Queue menggunakan module collections (class deque)
# import collections
# q = collections.deque() #membuat queue kosong
# print(q)
# q.append(30) #enque 30
# q.append(10) #enque 10
# q.append(20) #enque 20
# print(q)
# dihapus = q.popleft() #dequeue
# print(f'Elemen yang dihapus: {dihapus}')
# print(q)
# isEmpty = len(q)==0
# print(f'Queue kosong? {isEmpty}')
# print(f'Elemen front : {q[0]}')
# print(f'Elemen rear : {q[-1]}')

# # Implementasi queue menggunakan module queue (Class Queue)
# import queue
# q = queue.Queue() #membuat queue kosong
# print(q.queue)
# q.put(30) #enqueue
# q.put(10)
# q.put(20)
# print(q.queue)
# dihapus = q.get() #deque
# print(f'Elemen yang dihapus : {dihapus}')
# print(q.queue)
# print(f'Queue kosong ? {q.empty()}')
# print(f'Elemen front : {q.queue[0]}')
# print(f'Elemen rear : {q.queue[-1]}')

# Implementasi Queue menggunakan Linked List
class Element:
    def __init__(self, info):
        self.info = info
        self.next = None

class Queue:
    def __init__(self):
        self.front = None

    def view_element(self): #Method untuk melihat elemen
        if self.front is None: #Kondisi queue kosong
            print('Queue Kosong')
        else: #queue berisi elemen
            n = self.front
            while n.next is not None:
                print(n.info, end=',')
                n = n.next
            print(n.info)

    def enqueue(self, info): #method untuk enqueue (memasukkan elemen)
        new_element = Element(info)
        if self.front is None: #kondisi queue kosong
            self.front = new_element
        else: #queue berisi elemen
            n = self.front
            while n.next is not None:
                n = n.next
            n.next = new_element

    def dequeue(self): #menghapus elemen
        if self.front is None: #Kondisi queue kosong
            print('Tidak Menghapus elemen')
        elif self.front.next is None: #queue isi 1 elemen
            self.front = None
        else: #queue memiliki > 1 elemen
            self.front = self.front.next

    def view_front(self):
        if self.front is None:
            return '-'
        else : 
            return self.front.info
        
    def view_rear(self):
        if self.front is None:
            return '-'
        else : 
            n = self.front
            while n.next is not None:
                n = n.next
            return n.info

    def isEmpty(self):
        if self.front is None:
            return True
        else :
            return False

# Program utama
q = Queue()
q.enqueue(10)
q.enqueue(30)
q.enqueue(20)
# q.dequeue()
print(f'Elemen front : {q.view_front()}')
print(f'Elemen rear : {q.view_rear()}')
print(f'Queue kosong ? : {q.isEmpty()}')
q.view_element()