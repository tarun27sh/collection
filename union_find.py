import random

# AKA Disjoint-set data structure
class UnionFind():
    def __init__(self, n):
        self.no_of_sets = n                        # no of connected components
        self.parent     = [i for i in range(n)]        # parent of ith element, i itself
        self.no_of_elem = [0 for i in range(n)]    # no of elements with i as parent
        self.rank       = [0 for i in range(n)]    # ranks init to 0
        #self.rank = []

    def __str__(self):
        return 'no of sets= {}, parents = {}, no_of_ele = {}'.format(self.no_of_sets, self.parent, self.no_of_elem)

    # returns parent of the set
    def find(self, val):
        if self.parent[val] == val:
            return val
        else:
            return self.find (self.parent[val])

    def find_with_path_compression (self, val):
        if self.parent[val] == val:
            return val
        else:
            self.parent[val] = self.find_with_path_compression (self.parent[val])
            return self.parent[val]

    # merges two sets
    # attach tree with fewer elements to tree with having more elements
    def union_by_size (self, val1, val2):
        p1 = self.find_with_path_compression(self.parent[val1])
        p2 = self.find_with_path_compression(self.parent[val2])
        self.no_of_sets -= 1
        if p1 == p2:
            print('already in same set')
            return 
        else:
            # whoever has more elementes, make that parent
            if self.no_of_elem[p1] > self.no_of_elem[p2]:
                self.no_of_elem[p1] += self.no_of_elem[p2]
                self.parent[p2] = p1
            else:
                self.no_of_elem[p2] += self.no_of_elem[p1]
                self.parent[p1] = p2
        return

    # attach shorter tree to the root of taller tree
    def union_by_rank (self, val1, val2):
        if self.is_same_set(val1, val2):
            print('already in same set {}, {}'.format(val1, val2))
            return 
        p1 = self.find_with_path_compression(self.parent[val1])
        p2 = self.find_with_path_compression(self.parent[val2])
        self.no_of_sets -= 1
        print('adding {} and {}'.format(val1, val2))
        # whoever has greater rank, make that parent
        if self.rank[p1] == self.rank[p2]:
            self.rank[p1] += 1
            self.parent[p2] = p1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
        return

    def is_same_set(self, val1, val2):
        if self.find_with_path_compression(self.parent[val1]) == \
            self.find_with_path_compression(self.parent[val2]):
            return True
        return False

uf = UnionFind(100)
for x in range(1,100):
    curr1 = random.randint(0,99)
    curr2 = random.randint(0,99)
    uf.union_by_rank(curr1,curr2)

# print parents
for x in range(100):
    print('[{}] = {}'.format(x, uf.find_with_path_compression(x)))
print(uf.is_same_set(4, 5))
print(uf)
