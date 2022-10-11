"""
첫 줄에 로또 당첨번호 6개와 보너스 번호 1개가 주어진다.

둘째 줄에 지혜가 가지고 있는 로또 번호 6개가 주어진다.

 

출력
지혜의 당첨 결과를 출력한다.

출력방법) 

1등 = 1 출력, 2등 = 2 출력, 3등 = 3 출력, 4등 = 4 출력, 5등 = 5 출력, 꽝 = 0 출력
"""
# set 집합 자료형 써서 교집합으로 계산하자 교집합이 6이면 6개 같은거니까 1등이므로 1 출력 (교집합 intersection 메서드)
jihye = list(map(int,input().split()))
bonus = jihye[-1] # 보너스 번호 따로 변수 만들어서 저장
jihye.pop(-1) # 보너스 번호는 뺌
lotto = list(map(int,input().split()))
result = set(lotto).intersection(set(jihye)) # 교집합을 출력함
result = len(list(result)) # 교집합 원소의 개수

if result == 6 :
    print("1")
elif result == 5 :
    if bonus in lotto: # 보너스 번호를 포함하면
        print("2")
    else:
        print("3")
elif result == 4 :
    print("4")
elif result == 3 :
    print("5")
else:
    print("0")
