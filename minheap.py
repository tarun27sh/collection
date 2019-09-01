class mheap:
    def __init__(self, size):
        self.arr = []
        self.msize = size
        self.csize = 0

    def insert(self, val):
        if self.csize == self.msize:
            print('heap full!!')
        self.csize += 1
        self.arr.append(val)
        self.bubble_up(self.csize - 1) # index of last element

    def bubble_up(self, i):
        if not i:
            return
        #print('i={}, i/2={}, list={}'.format(i, i//2, self.arr))
        if self.arr[i//2] > self.arr[i]:
            self.arr[i//2], self.arr[i] = self.arr[i], self.arr[i//2]
            self.bubble_up (i//2)

    def pop(self):
        if self.csize==0:
            print('heap empty!!')
            return None 
        if self.csize==1:
            self.csize -= 1
            return self.arr.pop()
        tmp = self.arr[0]
        print('arr={}'.format(self.arr))
        self.arr[0] = self.arr.pop()
        self.csize -= 1
        self.bubble_down(0)
        print('after bubdown - {}'.format(self.arr))
        return tmp


    def bubble_down(self, i):
        if 2*i + 2 >= self.csize:
            return 
        if self.arr[i] > self.arr[2*i + 1] or self.arr[i] > self.arr[2*i + 2]:
            greater_index = 2*i +1 if self.arr[2*i + 1] < self.arr[2*i + 2] else 2*i+2
            print('swapping {} and {}'.format(self.arr[greater_index], self.arr[i]))
            self.arr[greater_index], self.arr[i] = self.arr[i], self.arr[greater_index]
            self.bubble_down(greater_index)

h = mheap(2**8)
for x in range(10, 0, -2):
    h.insert(x)

print('after insert: {}'.format(h.arr))

val = h.pop()
print('min = {}'.format(val))

while val:
    val = h.pop()
    print('min = {}'.format(val))
