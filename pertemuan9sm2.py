# # Implementasi Stack menggunakan struktur data list
# stack = [] # membuat stack kosong
# print(stack)
# stack.append(10) 
# stack.append(20) 
# stack.append(15) 
# print(stack)
# dihapus = stack.pop()
# print(f'Elemen dihapus : {dihapus}')
# print(stack)
# print(f'Elemen top: {stack[-1]}') #melihat elemen top
# isEmpty = len(stack) == 0
# print(f'Stack kosong? : {isEmpty}')


# # Implementasi Stack menggunakan module collections (class deque)
# import collections
# stack = collections.deque() # membuat stack kosong
# print(stack)
# stack.append(30) #push 30
# stack.append(10) #push 30
# stack.append(20) #push 30
# print(stack)
# dihapus = stack.pop()
# print(f'Elemen dihapus : {dihapus}')
# print(stack)
# print(f'Elemen top: {stack[-1]}')
# isEmpty = len(stack) == 0
# print(f'Stack kosong? : {isEmpty}')

# # Implementasi stack menggunakan modul queue (class LifoQueue)
# import queue
# stack = queue.LifoQueue() # membuat stack kosong
# print(stack.queue)
# stack.put(20) #push 20
# stack.put(10) #push 10
# stack.put(30) #push 30
# print(stack.queue)
# dihapus = stack.get() #pop
# print(f'Elemen dihapus : {dihapus}')
# print(f'Elemen top: {stack.queue[-1]}')
# isEmpty = len(stack.queue) == 0
# # print(f'Stack kosong? : {isEmpty}')
# # print(f'Elemen top: {stack.queue[-1]}')
# print(f'Stack Kosong ? : {stack.empty()}')
# print

class Element: #digunakan untuk membuat elemen baru
    def __init__(self, info):
        self.info = info
        self.next = None

class Stack: # digunakan untuk membuat stack dan run operasi
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        else :
            return False

    def view_top(self):
        if self.top is None:
            return '-'
        else :
            return self.top.info

    def view_element(self): #Method untuk melihat elemen-elemen stack
        if self.top is None: #kondisi stack kosong
            print('Stack Kosong')
        else: #kondisi stack berisi
            n = self.top
            while n.next is not None:
                print(n.info, end=',')
                n = n.next
            print(n.info)

    def push(self, info): #Method untuk operasi push
        new_element = Element(info)
        if self.top is None: #kondisi stack kosong
            self.top = new_element
        else : #kondisi stack berisi
            new_element.next = self.top
            self.top = new_element

    def pop(self): #method untuk operasi pop
        if self.top is None: #kondisi stack kosong
            print("Tidak bisa menghapus elemen")
        elif self.top.next is None: #stack satu elemen
            self.top = None
        else : #kondisi stack > 1 elemen
            self.top = self.top.next

# Program utama
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.pop()
st.view_element()
print(f'Elemen top : {st.view_top()}')
print(f'Stack kosong ? : {st.isEmpty()}')