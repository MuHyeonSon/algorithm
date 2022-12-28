# 튜플은 원소 순서 바뀌면 다른 튜플이고, 
# 중복되는 원소가 없는 튜플은 집합 기호를 이용해 표현이 가능하고
# 이때, 집합 안에 원소들은 순서 바뀌어도 상관 X
# 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.


# 우선 s가 표현하는 튜플을 찾는 방법은 원소 집합의 길이가 가장 작은 거 부터 찾는 거임
# (왜냐하면 가장 앞에 있는 원소만이 원소를 하나만 갖고 있는 집합원소가 될 수 있기 때문에)

# 그러면 문자열을 읽어 들여서 숫자를 split 해서 집어 넣어야 됨,


def solution(s):
    answer = [] # 최종 결과 저장할 리스트
    result = [] # s를 리스트로 만든 결과를 저장하기 위한 리스트
    part_set = [] # 튜플의 부분 집합을 저장할 리스트
    temp_s = ""  # 하나의 숫자정보를 저장하기 위한 변수 선언
    temp_list = [] # 중괄호 개수에 세서 집합의 원소집합 구분
    
    # s를 리스트로 만드는 과정
    for chr in s :
        # 만약 읽어들인 문자가 숫자라면
        if chr.isdigit() :
            temp_s = temp_s + chr # 숫자 문자열에 concatenate
        # 만약 읽어들인 문자가 숫자가 아니라면
        else :        
            # 하나의 숫자정보가 완성되었다면 (다음 문자 숫자X이고 그 문자열이 숫자로 구성되어있다면)
            if len(temp_s) != 0:
                part_set.append(int(temp_s))
                temp_s = ""  # 하나의 숫자정보를 저장하기 위한 변수 초기화
            
            # 만약 해당 문자가 중괄호라면
            if chr == "{" or chr == "}":
                temp_list.append(chr)
                # 중괄호가 끝나는 부분이면 
                # if "}" in temp_list and temp_list.asdasd("{") == 2:
            
                if ("{" in temp_list) and ("}" in temp_list) :
                    result.append(part_set)
                    part_set = []
                    temp_list = []
    
    # s에 대한 리스트로부터 s가 표현하는 튜플을 배열에 담기 (부분집합의 길이가 작은 것부터 처리)
    index = 0 
    length = 1
    while True:
        # 더이상 s에 대한 리스트에 원소가 남아있지 않다면
        if len(result) == 0:
            break
            
        if len(result[index]) == length :
            # 부분집합에서 이미 처리한 데이터가 존재하면 제거 
            for i in range(len(answer)):
                result[index].remove(answer[i])
            answer.append(result[index][0]) #제거 처리되어 하나가 남은 부분집합의 원소를 최종결과리스트에 append
            result.pop(index) # 처리된 부분집합은 s에 대한 리스트에서 제거
            index = 0
            length += 1
        else :
            index += 1
    
    return answer
    
    
    
    
# 느낀점 풀이시간 (1시간 53분)
"""
 - part_set = []
 - temp_list = []
이 두 개의 리스트를 clear로 초기화하니까 그 뒤에 append를 함에도 결과가
빈 리스트로 나와 문제가 계속해서 해결되지 않았었다.

일단 이번문제 또한 문제를 이해하는데 많은 시간이 소요되었으며
처리방식을 찾기 까지도 오랜시간이 소요되었다. 해결 방법을 찾았음에도
내가 찾은 방식을 사용한다면 2차원 리스트를 원소의 길이에 따라 오름차순으로 정렬하는 
코드를 작성하는 것이 어려웠다. 너무 비효율적으로 구현한 것이 아닌지에 대한 생각을 많이 하였고,
앞에서 언급한 두 개의 리스트가 문제를 발생시켜 이것을 해결하는 데 너무 많은
시간이 걸렸다.. 다른 사람의 풀이를 아직 보기 전인데 보고 나면
정말 간단하게 구현할 수 있었던 것을 나혼자 또 어렵게 구현한 것을 느끼게 된다면
자괴감을 느끼겠지만 이것 또한 성장하는 과정이라고 생각한다.
역시나 다른 사람들의 풀이를 보니 미친듯이 간단하게 풀리는 문제였다.
가장 인상깊었던 것은 정규표현식을 사용하여 처리한 분이 계셨는데
이것을 어떻게 적용하였는지 이해가 바로 되지 않았고, 숫자 부분만 남겼다고
하더라도 문제는 튜플의 원소 순서는 어떻게 구한 것인지도 잘모르겠다..
또한 그냥 숫자가 등장횟수로 비교하면 되는 것도 알게되어서 내가 너무 어렵게 푼 것을
알게되었다.

다른 사람의 풀이를 참고하여 연습하였을 때 다음과 같이 작성해보았다.

import re # 정규표현식관련
from collections import Counter # 숫자 카운트 관련

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

a = s
s = Counter(re.findall('\d+',s)) # re.findall은 정규표현식에 해당되는 문자열들을 모두 추출하여 그것들을 원소로한 리스트를 반환
                          
result = [int(k) for k, v in sorted(s.items(), key=lambda x : x[1], reverse =True)]
print(result)
########################
a = re.findall('\d+', a)
print(f're.findall결과 : {a}')
print(f's : {s}')
print(f's.items() : {s.items()}')

실행결과 :
[2, 1, 3, 4]
re.findall결과 : ['2', '2', '1', '2', '1', '3', '2', '1', '3', '4']
s : Counter({'2': 4, '1': 3, '3': 2, '4': 1})
s.items() : dict_items([('2', 4), ('1', 3), ('3', 2), ('4', 1)])

"""



"""
