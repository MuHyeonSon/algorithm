# 최대 10만명
# 1. 반복문 풀이 
# (둘의 겹치는 선수를 제외하고 나머지 한 선수만 구하면 됙 때문에 정렬후 다른 거 찾기)
'''
from collections import Counter
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
'''

# 2. Hash 사용
def solution(participant, completion):
    hashdict = dict()
    hashsum = 0
    
    # 해시 딕셔너리 만들기 (key(해시값) : data(선수명))
    for p in participant:
        hashdict[hash(p)] = p
        hashsum += hash(p)
    
    for c in completion:
        hashsum -= hash(c)
    
    return hashdict[hashsum]


# 느낀점 or 생각할점
"""
굉장히 간단한 문제라고 생각했지만, 이를 코드로 구현하는 것이 바로 떠오르지 않았다.
1번 풀이로는 for문을 이용해서 어차피 중복을 포함해 겹치지 않는 선수만 찾으면 된다라는 점을 이용해 정렬 후 한 명씩 확인하는 방법으로 풀었다.
2번 풀이는 hash를 사용한 풀이이며, 참가자들에 대한 모든 hash값을 계산하여 더하고, 완주한 선수들에 대한 hash값을 모두 빼면 완주하지 못한 한 선수에 대한 hash값만 
남게 된다는 것을 이용한 풀이다.
1번으로도 쉽게 풀리지만 hash라는 자료구조를 사용하는 것이 출제의도 였으므로 2번 풀이를 외부 검색을 통해 참고하여 풀 수 있었다.
"""
