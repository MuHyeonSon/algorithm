from seq_bin_search import*

class SequentialMap:
    def __init__(self):
        self.table = []
        
    def size(self): return len(self.table)
    
    def display(self,msg):
        print(msg)
        for entry in self.table:
            print(" ",entry)
    def insert(self,key,value) :
        self.table.append(Entry(key,value))
    
    def search(self,key):
        pos = sequential_search(self.table,key,0,self.size()-1)
        if pos is not None : return self.table[pos] #인덱스 값을 return
        else : return None
    
    def delete(self,key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

# 테스트 프로그램
map = SequentialMap()
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential search','선형 탐색')
map.insert('game','게임')
map.insert('binary search','이진 탐색')
map.display("나의 단어장: ")

print("탐색:game --> ",map.search('game'))
print("탐색:over --> ",map.search('over'))
print("탐색:data --> ",map.search('data'))

map.delete('game')
map.display("나의 단어장: ")