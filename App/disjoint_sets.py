import config as cf

from DISClib.ADT import map as mp
from DISClib.ADT import list as ls
from DISClib.DataStructures import linkedlistiterator as ll_it

class d_node:
    def __init__(self):
        self.ref = None
        self.rank = 1
    
    def join(self, other):
        other: d_node
        self_root = self.root()
        other_root = other.root()
        if self_root.rank < other_root.rank:
            self_root.ref = other_root
        elif self_root.rank == other_root.rank:
            self_root.ref = other_root
            other_root.rank += 1
        else:
            other_root.ref = self_root
    
    def root(self):
        if not self.ref:
            return self
        else:
            self.ref = self.ref.root()
            return self.ref

class disjoint_set_iterator:
    def __init__(self, set):
        self.list = mp.valueSet(set.hash_table)
        self.it = ll_it.newIterator(self.list)

    def __next__(self):
        if ll_it.hasNext(self.it):
            return ll_it.next(self.it)
        else:
            raise StopIteration

class disjoint_sets:
    def __init__(self, size):
        self.hash_table = mp.newMap(numelements=size)
    
    def add_node(self, key):
        mp.put(self.hash_table, key, d_node())
    
    def join(self, key1, key2):
        node1 = mp.get(self.hash_table, key1)['value']
        node2 = mp.get(self.hash_table, key2)['value']
        node1.join(node2)
    
    def root(self, key):
        node = mp.get(self.hash_table, key)['value']
        return node.root()

    def __iter__(self):
        return disjoint_set_iterator(self)
    
    def set_number(self):
        count = 0
        for node in self:
            if node.root() == node:
                count += 1
        return count