
from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.type=collision_type
        self.params=params
        self.table_size=params[-1]
        self.count=0
        if self.type=="Chain":
            self.table=[[] for _ in range(self.table_size)]
        else:
            self.table=[None]* self.table_size
        #"Chain": params = (z, table_size)
        # "Linear": params = (z, table_size)
        # "Double": params = (z1, z2, c2, table_size)
        # pass
    
    def insert(self, x):
        if self.type=="Chain":
            if  self.find(x)==False:
                i=self.get_slot_1(x)
                if i!=None:
                    self.table[i].append(x)
                    self.count+=1
                else:
                    raise Exception("Table is Full")
        else :
            if  self.find(x)==False:
                i=self.get_slot_1(x)
                if i!=None:
                    self.table[i]=x
                    self.count+=1
                else:
                    raise Exception("Table is Full")
        # print(self.count)       
                
        # pass
    
    
    def find(self, key):
        if self.type == "Chain":
            hash_value = self.hash_c(key, self.params[0], self.table_size)
            bucket = self.table[hash_value]
            
            # Check if the bucket is empty
            if bucket == []:
                return False
            
            # Search through the chain in the bucket
            return key in bucket  # Return True if key is found, otherwise False
        
        elif self.type == "Linear":
            # Start probing linearly from the calculated hash position
            i = self.hash_c(key, self.params[0], self.table_size)
            n = self.table_size
            j = 0
            
            # Linear probing to find the key
            while self.table[i] != None and j <= n:
                if self.table[i] == key:  # Check if the key matches
                    return True  # Key found
                j += 1
                i = (i + 1) % n
            
            return False  # Key not found

        elif self.type == "Double":
            # Start double hashing from the calculated positions
            i = self.hash_c(key, self.params[0], self.table_size)
            j = self.hash_d(key, self.params[1], self.params[2])
            n = self.table_size

            # Double hashing to find the key
            for t in range(n):
                current_pos = (i + t * j) % n
                if self.table[current_pos] == None:
                    return False  # Stop if an empty slot is found
                if self.table[current_pos] == key:  # Check if the key matches
                    return True  # Key found
            
            return False  # Key not found
    def get_slot(self, key):
        return self.hash_c(key, self.params[0], self.table_size)
    
    def get_slot_1(self, key):
        # pass
        if self.type=="Chain":
            return self.hash_c(key,self.params[0],self.table_size)
        elif self.type=="Linear":
            start=self.hash_c(key,self.params[0],self.table_size)
            table=self.table
            size=self.table_size
            i=start
            if table[start]==None:
                return start
            i=(i+1)%size
            while table[i]!=None and i!=start:
                i+=1
                i%=size
            if table[i]==None:
                return i
            return None
        else:
            n=self.table_size
            table=self.table
            i=self.hash_c(key,self.params[0],n)
            j=self.hash_d(key,self.params[1],self.params[2])
            for t in range(n):
                if table[(i+j*t)%n]==None:
                    return (i+j*t)%n
            return None
            
    def get_load(self):
        # pass
        return self.count/self.table_size

    def __str__(self):
        if self.type=="Chain" :
            result=[]
            for i in self.table:
                if i==[None]:
                    result.append("<EMPTY>")
                else :
                    result.append(" ; ".join(str(e) for e in i))
            return "|".join(result)
        else:
            result=[]
            for i in self.table:
                if i==[None]:
                    result.append("<EMPTY>")
                else :
                    result.append(str(i))
            return " | ".join(result)
        # pass
    def hash_c(self,key,z,size):
        # self.type=="Chain":
            s=str(key)
            hash_value=0
            # z=self.params[0]
            # n=self.table_size
            n=len(s)
            for i in range(n):
                hash_value=((hash_value*z+(self._char_to_value(s[n-1-i])))% size)
                # hash_value%=size
            return hash_value
        # elif self.type=="Linear":
            
        # else:
            # c2=self.params[2]
    def _char_to_value(self, char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 26
        return 0    
    def hash_d(self,key,z,c2):
        hash_value_c=self.hash_c(key,z,c2)
        return c2-hash_value_c
        
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
        # pass
    
    def insert(self, key):
        super().insert(key)
        # pass
    
    def find(self, key):
        return super().find(key)
        #     return False
        # else:
        #     return True
        # pass
    
    def get_slot_1(self, key):
        return super().get_slot_1(key)
        # pass
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        # pass
        return super().get_load()
    
    def __str__(self):
        results=[]
        for slot in self.table:
            if slot == [] or slot==None:
                results.append("<EMPTY>")
            elif self.type=="Chain" and len(slot)>0:
                results.append(" ; ".join((str(key)) for key in slot))
            else:
                results.append(str(slot))
        return " | ".join(results)
        # pass
        # return super().__str__()
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        # 
        super().__init__(collision_type, params)
        # pass
    
    def insert(self, x):
        # x = (key, value)
        # super().insert(x)
        if self.type=="Chain":
            if  self.find(x[0])==None:
                i=self.get_slot_1(x[0])
                # print(i)
                if i!=None:
                    # if self.table[i]==None:
                        # self.table[i].pop()
                    self.table[i].append(x)
                    # print(x)
                    self.count+=1
                else:
                    raise Exception("Table is Full")
        else :
            if  self.find(x[0])==None:
                i=self.get_slot_1(x[0])
                if i!=None:
                    self.table[i]=x
                    # print(x)
                    self.count+=1
                else:
                    raise Exception("Table is Full")
        
        # pass
    
    def find(self, key):
            if self.type == "Chain":
                hash_value = self.hash_c(key, self.params[0], self.table_size)
                bucket = self.table[hash_value]
                
                # Check if the bucket is empty
                if bucket == []:
                    return None
                
                # Search through the chain in the bucket
                for k, v in bucket:
                    if k == key:
                        return v  # Return value if key is found
                return None  # Return None if not found
            
            elif self.type == "Linear":
                # Start probing linearly from the calculated hash position
                i = self.hash_c(key, self.params[0], self.table_size)
                n = self.table_size
                j = 0
                
                # Linear probing to find the key
                while self.table[i] !=None and j <= n:
                    if self.table[i][0] == key:  # Check if the key matches
                        return self.table[i][1]  # Return the value if found
                    j += 1
                    i = (i + 1) % n
                
                return None  # Return None if not found

            elif self.type == "Double":
                # Start double hashing from the calculated positions
                i = self.hash_c(key, self.params[0], self.table_size)
                j = self.hash_d(key, self.params[1], self.params[2])
                n = self.table_size

                # Double hashing to find the key
                for t in range(n):
                    current_pos = (i + t * j) % n
                    if self.table[current_pos] == None:
                        return None  # Stop if an empty slot is found
                    if self.table[current_pos][0] == key:  # Check if the key matches
                        return self.table[current_pos][1]  # Return the value if found
                
                return None  # Return None if not found

        # pass
    
    def get_slot_1(self, key):
        return super().get_slot_1(key)
        # pass
    
    def get_load(self):
        # pass
        return super().get_load()
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def __str__(self):
        results=[]
        for slot in self.table:
            if slot == [] or slot==None:
                results.append("<EMPTY>")
            elif self.type=="Chain" and len(slot)>0:
                results.append(" ; ".join(f"({k}, {v})" for k,v in slot))
            else:
                results.append(f"({slot[0]}, {slot[1]})")
        return " | ".join(results)

# print(b)