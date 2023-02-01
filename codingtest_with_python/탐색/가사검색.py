# condingtest_with_python_part3_이진탐색
# 가사검색.py

# 나의 풀이 (교재 해설 참고)
from bisect import bisect_left, bisect_right

def find_match(words, q):
    left_q = q.replace("?", "a") # 와일드카드 문자를 모두 영문자중 가장 첫번째 값인 a로 변경
    right_q = q.replace("?", "z") # 와일드카드 문자를 모두 영문자중 가장 마지막 값인 z로 변경
    left = bisect_left(words, left_q)
    right = bisect_right(words, right_q)
    return right - left

def solution(words, queries):
    answer = [] # 결과 리스트
    # 키워드 길이와 단어길이가 맞아야되기 때문에, 각 키워드에 대해 길이가 같은 단어들만 고려해야하므로
    # 검색키워드의 길이가 [1, 10000]이므로 그 개수만큼 리스트 생성
    # 특정 글자 수의 단어들만 고려하도록 하기 위해 
    # 나의 경우는 글자수 대로 단어들을 정렬하고, 인덱스 정보를 담은 리스틀 따로 생성하고 
    # 그 글자수가 위치한 범위만 보기 위해 bisect_left와 bisect_right를 한 번씩 더 진행하였음.
    consider_length_words = [[] for _ in range(10001)]
    consider_length_words_reverse = [[] for _ in range(10001)] # 키워드의 와일드카드가 접두사인 경우를 위해
    # 해당 단어의 글자수에 해당되는 리스트에 해당 글자를 삽입함(거꾸로된 단어에 대해서도 마찬가지로 진행)
    for w in words:
        length = len(w)
        consider_length_words[length].append(w)
        consider_length_words_reverse[length].append(w[::-1])
    # bisect를 진행하기 위해 사전순으로 정렬함
    for i in range(1, 10001):
        consider_length_words[i].sort() # 사전 순으로 정렬(1/31에 이문제를 풀 때 헤맸던 이유는 바로 이것을 안해서)
        consider_length_words_reverse[i].sort()
    # 각 키워드 별로 매치된 단어가 몇 개인지 찾아 결과리스트에 저장
    for q in queries:
        # 검색 키워드의 와일드카드가 접미사라면
        if q[0] != '?':
            answer.append(find_match(consider_length_words[len(q)], q))
        # 검색 키워드의 와일드카드가 접두사라면
        else :
            answer.append(find_match(consider_length_words_reverse[len(q)], q[:: -1]))
    return answer


# 나의 풀이 (주어진 풀이 시간 : 분, 풀이 시간 : 분 초 )
## 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지
## 를 알려주는 프로그램 개발
## 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열
## ??는 딱 이 글자 개수로 어떤 것이든 들어와도 된다는 거임
## 정규표현식 사용? 아니면 ord 써서 알파벳 소문자만으로 구성되니까 a(97) ~ z(122)까지만
## ? 는 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어짐
## 결론 : 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열
## queries가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아
## 반환하도록 해라.

## 검색 키워드 개수가 10만개임키워드의 길이는 최대 10,000임 따라서
## 찾으려는 키워드의 총 글자 수는 최악의 경우 문자 수가 10,000,000,000 백억임
## 어찌 됐던간에 데이터가 이따구로 크면 이진탐색 이용해야됨
## 이진탐색 이용 : words에서 queries[i]의 개수를 찾는데 사용
## 이진탐색은 우선 아닌 것들은 반으로 걸러내야됨 그럴라면 정렬되어 있어야되
## 그리고 bisect도 적절히 활용해야됨 왜냐면 개수를 찾아야되잖아
## queries도 정렬해야되나? 왜냐면 이진탐색을 n번쓰면 결국 O(NlogN)이 되는 거잖아
## 근데 queries 자체는 데이터 개수가 최대 10만이니까 O(NlogN)해도 되지 않음?
## 그리고 bisect만으로는 글자수까지 정확히 고려하면서 못잡아냄 그니까
## queries에도 뭔가 조치를 취하던 길이대로 정렬하던해서 bisect를 두번 해야되지
## 않을까 왜냐면 진짜 bisect로 걸러서 단순히 하나씩 글자수 맞는 지 확인하는 식을 하면
## O(N) 됨.
## len써서 길이정보를 같이 이용해야 될 듯..

## 우선 words를 길이기준으로 정렬
## q[i]의 길이 범위내에서 bisect로 개수 찾기 => bisect 두번?
## ?? 는 접두사 아니면 접미사로 중 하나로만 주어진다고 했기 때문에, 단순히 양방향 고려해주면 됨

from bisect import bisect_left, bisect_right

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def find_match(words, words_length, q):
    length = len(q) # 해당 검색키워드의 길이정보 저장
    left_q = q.replace("?", "a") # 와일드카드 문자를 모두 영문자중 가장 첫번째 값인 a로 변경
    right_q = q.replace("?", "z") # 와일드카드 문자를 모두 영문자중 가장 마지막 값인 z로 변경
    
    # 가사 단어리스트에서 해당 검색 키워드의 길이의 문자가 위치해있는 범위에 대한 인덱스 정보를 구함
    left_index = bisect_left(words_length, length)
    right_index = bisect_right(words_length, length)
    #print(f'q : {q}')
    #print(f'length : {length}')
    #print(f'left_q : {left_q}')
    #print(f'right_q : {right_q}')
    #print(f'words[left_index:right_index] : {words[left_index:right_index]}')
    # 해당 쿼리에 부합하는 가사 단어들이 위치해있는 범위에 가장 왼쪽 인덱스와 가장 오른쪽 인덱스를 구함
    left = bisect_left(words[left_index:right_index], left_q)
    right = bisect_right(words[left_index:right_index], right_q)
    #print(f'words[right] : {list(words[left_index:right_index])[right]}')
    #print(f'left : {left}, right : {right}')
    #print(f'words[left:right] : {words[left:right]} ') 
    #print("------------------------------------------")
    return right - left

def solution(words, queries):
    answer = [] # 결과 리스트
    #words.sort() # 사전 순으로 정렬(1/31에 이문제를 풀 때 헤맸던 이유는 바로 이것을 안해줬기 때문임)
    words.sort(key = lambda x : [len(x), x]) # 글자 수를 기준으로 정렬 됨
    #print(f'정렬 후 words : {words}')
    words_length = [] # 각 가사의 단어들의 길이를 기록할 리스트
    words_reverse = [] # 와일드카드 문자가 접미사일 경우를 위해 각 단어들을 거꾸로한 단어들을 저장할 리스트 
    # 각 단어들의 길이를 저장하고, 각 단어에 대한 거꾸로된 문자 저장
    for w in words:
        words_length.append(len(w))
        words_reverse.append(w[::-1])
    #words_reverse.sort() # 사전순으로 정렬
    words_reverse.sort(key = lambda x : [len(x), x]) # 글자 수를 기준으로 정렬됨
    # queries에서 검색 키워드를 하나씩 불러와서 해당 검색 키워드에 매치되는 단어가 몇 개인지 구하기
    for q in queries:
        # 검색 키워드의 와일드카드가 접미사라면
        if q[0] != '?':
            answer.append(find_match(words, words_length, q))
        # 검색 키워드의 와일드카드가 접두사라면
        else :
            answer.append(find_match(words_reverse, words_length, q[:: -1]))
    return answer

## 내 생각엔 words_length라는 놈을 따로 생성하기 때문에 시간초과가 발생하는 것 아닐까?
## 내가 지금 bisect를 총 4번 이용하는게 문제임

# 교재 풀이
from bisect import bisect_left, bisect_right

## 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, left_value)
    left_index = bisect_left(a, right_value)
    return right_index - left_index

## 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
## 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입
    
    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reverse_array[i].sort()
    
    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer
        


# 느낀점
"""
1. 아이디어는 해설에서 설명한대로 잘 떠올렸지만,

2. 구현 중에 초기에 사전 순대로 정렬하지 않아, 이부분을 찾는데 오랜 시간이 소요되었으며,
떠올린 아이디어를 그래도 코드에 옮겼음에도 2개의 테스트케이스가 시간초과로 통과하지 못했다. 

3. 내 코드에는 bisect_left와 bisect_right를 2번씩 사용해서 이부분이 시간복잡도를 늘렸던 것인지

4. 모르겠지만 교재해설처럼 키워드에 글자수와 동일한 단어들만을 고려하는 것을 따로 2차원 리스트를 생성해서
그것에 맞추어 코드를 바꾸어주었더니 모든 테스트케이스가 통과했다.

5. 이러한 방식을 절대로 잊지 않고 비슷한 문제가 나온다면 반드시 맞출 것이다.

6. 또한 교재에서 아예 함수로 정의해놓은 count_by_range를 그대로 이용한 것을 보고서,
나 또한 이 함수자체를 기억하는 것도 나쁘지 않을 것이라는 생각을 했다.
"""
