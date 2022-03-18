from class_Stack import*

inp = input("회문 체크용 문자열 : ")
inp = inp.lower() #입력받은 문자열의 알파벳들을 모두 소문자로 변환
inp = inp.strip() #입력받은 문자의 양옆에 있는 스페이스를 제거
s = Stack()
Str = []
for i in inp:
    if i.isalpha(): #in 함수를 사용하는 대신 isalpha를 사용하여 영문자만 추출
        s.push(i) 
        Str.append(i)
    else : continue

Str_join = ''.join(Str) #소문자인 영문자만 남기도록한 문자열을 저장할 변수

while not s.isEmpty():   #s가 비어 있지 않으면 계속 실행
  if s.pop() != Str.pop(0):  #s의 마지막 원소와 Str의 첫번째 원소가 다르다면
    print(f'{Str_join} : 회문아님!!') # 회문이 아니라고 출력
    break   # 반복문 탈출

if s.isEmpty():          #s가 비어있다면 s와 Str에서 원소를 하나씩 꺼냈을 때 모두 같았던 것이므로
  print(f'{Str_join} : 회문임!!') #회문이라고 출력
        


#inp = ''.join(s)
#print(inp)
