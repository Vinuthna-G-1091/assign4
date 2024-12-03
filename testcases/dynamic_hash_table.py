from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        # print(self.table_size)
        # print(self.count)
        # print(self.get_load())
        new_size=get_next_size()
        # print()
        self.table_size=new_size
        # print(self.get_load())
        old_table=self.table[:]
        # print(old_table)
        if self.type=="Chain":
            self.table=[[] for _ in range(new_size)]
            self.count=0
            for list in old_table:
                if list !=[]:
                    for i in list:
                        self.insert(i)
        else:
            self.table=[None]*(new_size)
            self.count=0
            for i in old_table:
                if i !=None:
                    self.insert(i)
        # pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size=get_next_size()
        self.table_size=new_size
        old_table=self.table[:]
        if self.type=="Chain":
            self.table=[[] for _ in range(new_size)]
            self.count=0
            for lis in old_table:
                if lis!=[]:
                    for i in lis:
                        self.insert(i)
        else:
            self.table=[None] *(new_size)
            self.count=0
            for i in old_table:
                if i !=None:
                    self.insert(i)
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()