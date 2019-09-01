'''
for alive cell
    nei < 2      -> die
    nei =2 or =3 -> live
    nei >3       -> die
for dead cell
    nei =3       -> live
'''
import time
import random               # to start with random board
import logging

logging.basicConfig(level=logging.ERROR)
class Grid:
    matrix = [[]]
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = [[random.randint(0,1) for y in range(col)] for x in range(row)]
        #self.matrix = [[1 for x in range(row)] for y in range(col)]
    def get_empty_matrix(self):
        return [[0 for x in range(self.col)] for y in range(self.row)]

    def get_neigh(self, x, y):
        count=0
        if x-1>=0:
            if self.matrix[x-1][y]:
                count+=1
        if x+1<self.row:
            if self.matrix[x+1][y]:
                count+=1
        if x-1>=0 and y+1< self.col:
            if self.matrix[x-1][y+1]:
                count+=1
        if y+1 < self.col:
            if self.matrix[x][y+1]:
                count+=1
        if x+1<self.row and y+1< self.col:
            if self.matrix[x+1][y+1]:
                count+=1
        if x-1>=0 and y-1>=0:
            if self.matrix[x-1][y-1]:
                count+=1
        if y-1>=0:
            if self.matrix[x][y-1]:
                count+=1
        if x+1<self.row and y-1>=0:
            if self.matrix[x+1][y-1]:
                count+=1
        return count
        
    def next_turn(self):
        mat = self.get_empty_matrix()
        for x in range(self.row):
            for y in range(self.col):
                neigh = self.get_neigh(x,y)
                if self.matrix[x][y]:   # alive
                    logging.debug('{},{} = alive'.format(x,y))
                    mat[x][y] = 1
                    if neigh<2 or neigh>3:
                        logging.debug('{},{} = alive -> dead'.format(x,y))

                        mat[x][y] = 0
                else:                   # dead
                    logging.debug('{},{} = dead'.format(x,y))
                    if neigh==3:
                        logging.debug('{},{} = dead -> alive'.format(x,y))
                        mat[x][y] = 1
        self.matrix = mat

    def display(self):
        print('matrix')
        for x in self.matrix:
            print(x)

    def clear_console(self):
        print('\033[H')

    def display_fancy(self):
        for x in self.matrix:
            str_=''
            for y in x:
                if y==1:
                    str_+=' o '
                else:
                    str_+=' . '
            print(str_)


                
        pass

grid_ob = Grid(50,50)
for x in range(40):
    grid_ob.clear_console()
    #grid_ob.display()
    grid_ob.display_fancy()
    grid_ob.next_turn()
    time.sleep(1)
