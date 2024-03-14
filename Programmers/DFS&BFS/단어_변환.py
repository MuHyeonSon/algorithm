from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    distances = [1e9 for _ in range(len(words))]
    #words.insert(0, begin) # 일허게 하면 무조건 안됨
    #distances.insert(0, 0)
    queue = deque([begin]) # 시작 단어 
    for i in range(len(words)):
        if calc_num_trans(begin, words[i]) == 1:
            queue.append(words[i])
            distances[i] = 1
            break
    distance = 0
    
    while queue:
        word = queue.popleft()
        if word not in words:
            distance = 0
        else:
            distance = distances[words.index(word)]
        #index 함수는 배열에서 값의 위치를 찾아주는 함수리며, 중복된 값이 있으면 가장 최소의 위치를 리턴
        for i in range(len(words)): #range(index + 1, len(words)):
            if calc_num_trans(word, words[i]) == 1 and distances[i] > distance: #and distances[index] == 0:
                queue.append(words[i])
                distances[i] = distance + 1
    print(distances)
    if distances[words.index(target)] >= 1e9:
        return 0
    return distances[words.index(target)]

def calc_num_trans(source, target):
    count = 0
    for i in range(len(source)):
        if source[i] != target[i]:
            count += 1
    return count

'''
단어 변환 문제를 BFS로 접근하여 최소 변환 횟수를 찾는 것으로
words에서 한 차례에 단어하나만 바꿔도 되는애를 다 큐에 넣고 거리를 저장하는 방식으로
아이디어를 떠올릴 수 있었지만, 떠올리지 못했던 디테일한 부분은 아래와 같다.
1. words가 정렬되어 있지 않아 words의 일부가 아닌 전체를 둘러봐야된다는 점.
2. 1번은 실행했을 때, 짧은 거리가 기존보다 큰 거리로 덮어씌워지지 않도록 더 작을 경우에만 distance를
  업데이트하기 위해 그 조건문을 추가하고 초기에 distance의 모든 원소를 무한대(1e9)로 초기화해야된다는 점.
3. 큐 자료구조에 시작값을 넣을 때 index와 distance를 구하기 위해 
'''

'''
hit hat hot lot log kog cog
words에서 탐색해야됨 한 차례에 단어하나만 바꿔도 되는애를 다 추가해야됨
hit에서 hat혹은 hot으로 가야될거야 여기다가 1을 추가하고
hat에서 lot으로 갈 수 없으니 1에서 멈추고
hot에서 lot으로 갈 수 있으니 +1해서 2를 저장
dfs로 해야될까 bfs로 해야될까
만약 하나만 차이가 나면 자료구조에 넣고
방문처리
만약 target과 같다면 answer 출력
상하좌우 뿐만 아니라 두개로 갈라지는 경우도 dfs로 풀수있었잖아
이미 계산했던 것을 이용함으로써 계산 줄이기
'''

# 이거 대학교 알고리즘 수업에서 했었음
#1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
#2. words에 있는 단어로만 변환할 수 있습니다.
# 변환할 수 없는 경우 0을 return
