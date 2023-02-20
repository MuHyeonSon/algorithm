# condingtest_with_python_part3_최단경로
# 정확한순위.py

# 나의 풀이

## 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 11분 46초 )
## 도대체 이 문제가 최단거리와 무슨 연관이 있을 까?
## 단순히 모든 애들로 부터 연결되어 있는 노드를 끝까지 따라갔을 때
##  v - 1만큼의 수가 나온다면 그 노드는 성적순위를 정확히 알 수 있는 방식으로 될까?
## 다시 생각해보면.. 
## 모든 지점에서 다른 모든지점까지의 최단거리 vs 한 지점에서 다른 모든지점까지의 최단 거리
## 모든 지점인 것같아.. 2차원 dp 테이블 만들어서
"""

INF = 1e9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] == 0
for _ in range(m):
    # a학생이 b보다 성적이 낮다 (a < b)
    a, b = map(int, input().split())
    graph[a][b] = a # a는 b보다 작다(작은 애를 저장)
    
## 그니까 여기서의 최단거리의 의미는? a가 b보다 작다고 저장했는데 만약 k가 a보다 작으면 
## k < a < b 이면 graph[a][b]로 가는 데에 아니면 a, b사이에 차이가 더 작은애가 있다? a < k < b
## if a < k:
##   graph[b][a] = 0
##   graph[b][k] = k
## a가 b보다 크면 b가 a를 가리킴
## 둘 중 하나라도 가리킨다면 그거는 성적 비교가 가능한거임
## 그럼 둘 중 하나라도 가리키는 애의 수를 중복되지 않게 구하면 되는 거임?
## 문제는 순위를 정확히 알 수 있는 애의 수를 구하는 거잖아

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # i랑 더 가까운 애를 (j와 k중 더 작은 것을 선택) 
            graph[i][j] = min(graph[i][j], graph[i][k])

result = 0
temp = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (graph[i][j] == INF or graph[i][j] == 0) or  (graph[i][j] == INF or graph[i][j] == 0):
            pass
        else:
            if set([i, j]) in temp:
                pass
            result += 1
            temp.append(set([i, j]))
            
print(result)                
                                    
"""            

    
    
# 교재 풀이
INF = int(1e9)

## 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
## 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

## 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
## 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

## 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
## 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0 # i번째 학생에 대해 성적이 비교가 가능한지 체크
                # i번 학생보다 성적이 높거나 낮은 학생들을 모두 아는 경우를 구함
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    ## i번 학생과 성적비교가 가능한 학생이 n과 같다면                
    if count == n:
        result += 1 # 순위를 정확히 할 수 있는 학생 1명 추가

print(result)

# 느낀점
"""
해당 문제가 최단거리와 어떠한 연관이 있는 지 생각해는 것이 무척어려웠다.
최단 거리를 구한다는 것이 학생들의 성적비교와 무슨 연관이 있는 것인지도
생각하기 어려웠는데 결국 최단거리를 구한다는 것은 성적 비교가 가능함을
구하기 위해서 였고, 모든 학생에 대해 최단거리를 구한 뒤에,
노드 관점에서 둘 중 하나가 다른 하나로 연결되어 있다면 성적 비교가 가능한 것이고
1번부터 n번 학생에 대해 1명씩 전체 n명에 대해 모두 연결되어 있다면
그 학생은 정확한 순위를 알 수 있다는 것이다.
교재를 참고한 뒤 위와 같은 방식을 이해할 수 있게 되었다..
모르는 문제였으니 꼭 기억해야겠다..
"""
