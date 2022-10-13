"""
암호학에서 시저 암호(Caesar cipher)는 가장 오래된 암호 중 하나이고, 가장 대표적인 대치(substitution) 암호로서 평문 문자를 다른 문자로 일대일 대응시켜 암호문을 만들어 낸다.

시저 암호는 알파벳을 3글자씩 밀려서 쓰면서 문장을 만들었다. 실제 시저는 부하인 브루투스에게 암살되기 전에 키케로에게 다음과 같은 암호문을 보냈다고 한다.

 

암호문

qhyhu wuxvw euxwxv

원문

never trust brutus

 

암호문을 원문으로 바꾸는 원리는 간단하다. 암호문에 쓰인 알파벳보다 3만큼 이동한 알파벳으로 치환하면 된다.

암호

a->x b->y c->z d->a

 

시저의 암호문이 입력되면 원문으로 복원하는 프로그램을 작성하시오.

 

입력
공백이 있는 영어 문자열이 최대 200글자 입력된다. 단, 공백과 알파벳 소문자외에 다른 문자는 입력되지 않는다.

출력
암호문을 원문으로 복원하여 출력하시오.

 

입력 예시   
qhyhu wuxvw euxwxv

출력 예시
never trust brutus
"""

caesar_list =     ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
original_list =   ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']

cipher = input()
original = '' # 원문 구해서 저장할 변수 초기화

for x in cipher:
    if x != ' ': # 공백 문자가 아니라면
        i = caesar_list.index(x) # cipher문자열 중 해당 차례에서 가져온 하나의 문자를 암호문 리스트에서 위치를 찾음
        original = original + original_list[i]
    else: # 공백 문자라면
        original = original + x
    
print(original) # 원문 출력

