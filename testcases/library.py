import hash_table as ht
from dynamic_hash_table import*
import copy
class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
        # self.titles=[]
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        # pass
        # super().__init__()
        # self.titles=self.merge_sort(book_titles)
        
        self.distinct_text=[]
        # self.texts=texts
        n=len(texts)
        inter =texts[:]
        # inter=[]
        # for i  in range(n):
        #     inter.append(texts[i])
# inter=texts[]
        for i in range(n):
            # print(texts[i])
            # inter[i]=texts[i]
            inter[i]=self.merge_sort(inter[i])
            # print(texts[i])
            ans=[]
            for w in inter[i]:
                if ans==[]:
                    ans.append(w)
                elif ans[-1]!=w:
                    ans.append(w)
            self.distinct_text.append(ans)
        lib=[]
        for i in range(len(book_titles)):
            lib.append((book_titles[i],self.distinct_text[i],texts[i]))
        # lib=list(zip(book_titles,self.distinct_text,texts))
        self.titles=self.merge_sort(lib)
        # self.texts=texts
    def merge(self, left, right):
        sorted_array = []
        left_index = right_index = 0
        
        # Compare elements from both halves and add the smaller one to the sorted array
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1
        
        # Append remaining elements from left or right
        sorted_array.extend(left[left_index:])
        sorted_array.extend(right[right_index:])
        
        return sorted_array

    def merge_sort(self, arr):
        # Base case: If the array has 1 or 0 elements, it's already sorted
        if len(arr) <= 1:
            return arr
        
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort each half and merge them
        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)
        
        return self.merge(left_sorted, right_sorted)



    def binary_search(self,arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if the target is at mid
            if arr[mid][0] == target:
                return mid
            # If the target is greater, ignore the left half
            elif arr[mid][0] < target:
                left = mid + 1
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1
        
        # Target is not present in the array
        return -1
    def binary_search_k(self,arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if the target is at mid
            if arr[mid] == target:
                return mid
            # If the target is greater, ignore the left half
            elif arr[mid] < target:
                left = mid + 1
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1
        
        # Target is not present in the array
        return -1

    def distinct_words(self, book_title):
        index=self.binary_search(self.titles,book_title)
        # book=self.titles[index]
        # print(book)
        return self.titles[index][1]
        # pass
    
    def count_distinct_words(self, book_title):
        index=self.binary_search(self.titles,book_title)
        return len(self.titles[index][1])
        # pass
    
    def search_keyword(self, keyword):
        ans=[]
        n=len(self.titles)
        for i in range(n):
            if self.binary_search_k(self.titles[i][1],keyword)!=-1:
                ans.append(self.titles[i][0])
        return ans
        # pass
    
    def print_books(self):
        books=[]
        for i in range(len(self.titles)):
            books.append(f"{self.titles[i][0]}: {' | '.join(self.titles[i][1])}")
        print("\n".join(books))
        # pass
        # ans=[]
        # for i in len(self.titles):
        #     # ans.append([i[0],i[1].__str__()])
        #     ans.append([self.titles[i],self.distinct_text[i]])
        # for j in ans:
        #     print(j[0]+": "+t+" | "for t in j[1])
        # result=[]
        #     for i in self.table:
        #         if i==[None]:
        #             result.append("<EMPTY>")
        #         else :
        #             result.append(str(i))
        #     return " | ".join(result)

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        if name=="Jobs":
            self.type="Chain"
            
        elif name=="Gates":
            self.type="Linear"
        else:
            self.type="Double"
        self.params=params
        self.books=[]
        # self.book_titles=DynamicHashMap(self.type,self.params)
        self.book_titles=ht.HashMap(self.type,self.params)
        # print(self.book_titles.table)
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        # pass
    
    def add_book(self, book_title, text):
        # params=self.params
        # n=len(params)
        # new_len=2*len(text)+1
        # if(n==2):
        #     new_params=(params[0],new_len)
        # else:
        #     new_params=(params[0],params[1],params[2],new_len)
        # new_params=self.params
        set=ht.HashSet(self.type,self.params)
        # set=DynamicHashSet(self.type,self.params)
        for t in text:
            # print(t)
            set.insert(t)
        # print(set.table)
        self.book_titles.insert((book_title,set))
        self.books.append((book_title,set))
        # print(self.book_titles.table)
        # pass
    
    def distinct_words(self, book_title):
        
        set=self.book_titles.find(book_title)
        # print("vinuthna",set.table)
        ans=[]
        if set!=None:
            table=set.table
                
            if self.type=="Chain":
                for i in table:
                    if i!=[]:
                        for j in i:
                            ans.append(j)
                    
            else:
                for i in table:
                    if i!=None:
                        ans.append(i)
                    
        # print("Vinuthna",ans)
        return ans
        # pass
    
    def count_distinct_words(self, book_title):
        return self.book_titles.find(book_title).count
        # pass
    
    def search_keyword(self, keyword):
        ans=[]
        # if self.type=="Chain":
        #     for i in self.book_titles.table:
        #         if i!=[]:
        #             # print(i[0][1].table)
        #             for j in i:
        #                 if(j[1].find(keyword)):
        #                     ans.append(j[0])
        #     return ans
        # else:
        #     for i in self.book_titles.table:
        #         if i!=None:
        #             # print(i[0])
        #             if(i[1].find(keyword)):
        #                 ans.append(i[0])
        #     return ans
        # if self.type=="Chain":
        for i in self.books:
            if(i[1].find(keyword)):
                ans.append(i[0])
        return ans
        # else:
        #     for i in self.book_titles.table:
        #         if i!=None:
        #             # print(i[0])
        #             if(i[1].find(keyword)):
        #                 ans.append(i[0])
        #     return ans
        
        # pass
    
    def print_books(self):
        ans=[]
        if self.type=="Chain":
            for i in self.book_titles.table:
                if i!=[]:
                    for j in i:
                        ans.append([j[0],j[1].__str__()])
        else:
            for i in self.book_titles.table:
                if i!=None:
                    # for j in i:
                    ans.append([i[0],i[1].__str__()])
        for j in ans:
            print(j[0]+": "+j[1])
        # pass
        # for book in self.book_titles.table:
        #     if not(book==[] or book==None):
        #         word=
        
