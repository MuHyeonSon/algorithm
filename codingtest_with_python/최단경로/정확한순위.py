# condingtest_with_python_part3_최단경로
# 정확한순위.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 11분 46초 )
## 도대체 이 문제가 최단거리와 무슨 연관이 있을 까?
## 단순히 모든 애들로 부터 연결되어 있는 노드를 끝까지 따라갔을 때
##  v - 1만큼의 수가 나온다면 그 노드는 성적순위를 정확히 알 수 있는 방식으로 될까?
## 다시 생각해보면.. 
## 모든 지점에서 다른 모든지점까지의 최단거리 vs 한 지점에서 다른 모든지점까지의 최단 거리
## 모든 지점인 것같아.. 2차원 dp 테이블 만들어서

INF = 1e9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] == 0
for _ in range(m):
    a, b = map(int, input().split())

    
    
# 교재 풀이


# 느낀점
"""

"""

"""
📰 Codingtest_with_python_part3_최단경로_정확한순위
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 최단경로 문제 풀이 느낀점
"""
