바이오메디컬공학부 201804594 손무현

from ArrayList import*

s1 = ArrayList()
s1.display('파이썬 리스트로 구현한 리스트 테스트 : ')
s1.insert(0,10); s1.insert(0,20); s1.insert(1,30)
s1.insert(s1.size(),40); s1.insert(2,50)
s1.display("파이썬 리스트로 구현한 리스트 삽입*5 : ")
s1.sort()
s1.display("파이썬 리스트로 구현한 리스트 정렬후 : ")
s1.replace(2,90)
s1.display("파이썬 리스트로 구현한 리스트 교체후 : ")
s1.delete(2); s1.delete(s1.size() - 1); s1.delete(0)
s1.display("파이썬 리스트로 구현한 리스트 삭제*3 : ")
lst = [1,2,3]
s1.merge(lst)
s1.display("파이썬 리스트로 구현한 리스트 병합후 : ")
s2 = ArrayList()
s2.insert(0,6); s2.insert(0,5); s2.insert(0,4)
s1.merge_2(s2)
s1.display("파이썬 리스트로 구현한 리스트 병합후 : ")
s1.clear()
s1.display("파이썬 리스트로 구현한 리스트 클리어 : ")


from ArrayList import*

def myLineEditor():
    listA = ArrayList()
    while True:
        command = input('[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ')
        
        if command == 'q' : return
        
        elif command == 'i':
            pos = int(input('입력할 행번호: '))
            str1 = input('입력 내용: ')
            listA.insert(pos,str1)
        
        elif command == 'd':
            pos = int(input('삭제할 행번호: '))
            listA.delete(pos)
            
            
        elif command == 'r':
            pos =int(input('수정할 행번호 : '))
            str1 = input('수정 내용 :')
            listA.replace(pos, str1)
        
        elif command == 'p':
            print('Line Editor')
            for line in range(listA.size()):
                print('[{:2d}] '.format(line), end='')
                print(listA.getEntry(line))
            print()     
 
        elif command == 'l':
            infile = open('test.txt','r')
            lines = infile.readlines()
            for line in lines:
                listA.insert(listA.size(), line.rstrip('\n'))
                infile.close()
        elif command == 's':
            outfile = open('test.txt','w')
            for i in range(listA.size()):
                outfile.write(listA.getEntry(i)+'\n')
            outfile.close()
        
myLineEditor()
