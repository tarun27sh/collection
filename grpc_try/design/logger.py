from collections import deque
class Logger:
    def __init__(self, size):
        self.msize=size    # in bytes
        self.csize=0
        self.msgs=deque()

    def log(self, t, msg):
        print('adding {} bytes'.format(self.strlen(msg)))
        if self.is_full():
             self.make_space(self.strlen(msg)+1) 
        self.msgs.append((t,msg))
        self.csize += self.strlen(msg)
        self.csize += 1   # tuple type

    def is_full(self):
        if self.csize >= self.msize:
            return True
        return False

    def make_space(self, msize):
        print('make space for {} bytes'.format(msize))
        while self.csize + msize >= self.msize and self.msgs:
              msg = self.msgs.popleft()
              self.csize -= self.strlen(msg[1] ) + 1

    def strlen(self, msg):
        return len(msg)*8

    def print(self):
        print('current size: {}, max: {}'.format(self.csize, self.msize))
        for x in self.msgs:
            print(x[0],':', x[1])

logger = Logger(10000)
msg='1'
for x in range(100):
    msg+='1'
    logger.log(len(msg)%2, '{} {}'.format(x, msg))
logger.print()

