# condingtest_with_python_part3_구현
# 문자열압축.py



# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 30 분, 풀이 시간 : 60분 초)    
"""
from collections import Counter
import itertools



def solution(s):
    answer = 1001
    length = len(s)
    if len(s) == 1 or len(s) == 2:
        return len(s)
    for i in range(1, len(s)//2):
        count = 1
        temp_s = ""
        temp_list = []
        for j in range(len(s),i):
            if j + (2*i) < len(s):
                if s[j:j+i] == s[j+i:j+(2*i)]:
                    count += 1
                else:
                    if count > 1:
                        length += len(str(count) + s[j:j+i])
                        temp_s += str(count) + s[j:j+i]
                        count = 1
                    else:
                        temp_s += s[j:j+i]
        length = len(temp_s)
        answer = min(answer, length)
        
        for l in temp_list:
            temp_s.replace()
            length += len(s) - len(temp_s)
    
        

        #for j in range(len(s)):
        #    if (2 * i) < len(temp_s):
        #        if temp_s[j:i] == temp_s[i:2*(i)]:
        #            temp_s[j:2*(i)] = temp
    
    

    ingredient = list(Counter(s))
    # 문자를 i개 단위로 잘라서 압축
    for i in range(len(s)//2):
        case_list = list(itertools.permutations(ingredient,i))
        temp_case_list = []
        for case in case_list:
            s_case = ""
            for c in case:
                s_case += c
            temp_case_list.append(s_case)
        temp_s = s
        temp_list = []
        length = 0
        for case in temp_case_list:
            if case in temp_s:
                length += temp_s.count(case)
                
        
    #                           
    #    answer = min(answer, length)
    print(len(Counter(s)))
    print(list(itertools.permutations(ingredient,2)))
    return answer


#카운터로 해당 문자열의 모든 구성원소 찾고 그걸 리스트로 만들어서
#permutation써 갖고 거기서 i 개 뽑아서 만들 수 있는 경우 모두 추출한 뒤에
#그 경우 (i개 + len(str(해당 반복문자열의 개수))) + .. 모든 경우를 다 더함
"""

# 교재 풀이
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step 만큼의 문자열 추출
        count = 1
        # 단위(step) 크기마늠 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면 (더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
            
        


# 느낀점
"""
문제를 제대로 파악하지 못해 헤맸던 부분은 다음과 같다.
1. 스텝 단위로 보는 것이 아니라 모든 인덱스 위치 하나하나 마다
    압축문자열이 만들어 질 수 있는 지를 고려해야 된다고 생각했다.
    가령 dababab 이러한 문자열 입력이 들어왓을 때, 압축문자열의 길이가 2라고 하면
    d ababab 이렇게 2번째 부터 시작해서 d3ab 이렇게도 만들 수 있어야된다고 생각했지만
    문제에서 요구하는 것은 첫번째 글자부터 무조건 포함한다는 것을 해설을 보고 알았다.
    만약 문제에서 요구하는 대로 한다면 da2bab 이렇게 되기 떄문에 두 번째부터 읽을 경우가 더 짧다.
    
    => 문제를 풀 떄 문제예시를 잘 살펴봐야겠다. (내 맘대로 해석하는 것은 문제를 풀 떄에 있어서 정말 잘못된 태도라는 것을 느꼈다.)

문제와 해결법이 같았지만 끝내 구현해내지 못한 부분은 다음과 같다.
1. 압축된 문자열을 제외하고 나머지 문자열에 대해서 처리하는 방법을 구현하지 못함.
    => 내가 파이썬 문자열 인덱싱에 대해서 똑바로 알지 못했다는 것을 다시 알게 됐다.
        s = "aabc"
        print(s[2:12315412342])
        이것의 출력결과는 bc 이다.
        난 이게 index out of range 가 뜰 줄 알고 어떻게 해야될 지 계속 고민했던 것이다.

또한 해설문제풀이는 너무나 깔끔하다는 것을 느꼈다.
     
하지만 위에서 언급한 부분들을 제외하고는 전체적인 프로그램의 구조가 내가 작성한 것과 비슷하였다고 느꼈다.
세부적인 부분을 구현해내지 못했고, 문제파악을 제대로 하지 못해 최종적으로 구현하지 못했던 것이 아쉬웠다.
"""
