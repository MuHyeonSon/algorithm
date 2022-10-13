"""
※ 씨저의 암호 원리는 앞의 문제를 참고하세요.

 

대현이는 씨저의 암호 방식을 이용하여 문장을 만들려고 한다.

never trust brutus 를 씨저의 암호로 바꾸면 qhyhu wuxvw euxwxv 이다.

 

그런데 집중력이 약한 대현이는 하나 하나 찾아서 암호로 바꾸는데 어려움을 겪고 있다.

우리가 대현이를 위해 평문을 씨저의 암호문으로 바꾸는 프로그램을 만들어주자.

 
"""
caesar_list =     ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
original_list =   ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']

original = input()
cipher = '' # 암호문 구해서 저장할 변수 초기화

for x in original:
    if x != ' ': # 공백 문자가 아니라면
        i = original_list.index(x) # cipher 문자열 중 해당 차례에서 가져온 하나의 문자를 암호문 리스트에서 위치를 찾음
        cipher = cipher + caesar_list[i]
    else: # 공백 문자라면
        cipher = cipher + x
    
print(cipher) # 원문 출력
