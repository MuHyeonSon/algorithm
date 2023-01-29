# condingtest_with_python_part3_정렬
# 안테나.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 분 초 )
n = int(input())
pos = list(map(int, input().split()))

result = []

for i in range(len(pos)):
    dist = 0
    for p in pos:
        dist += abs(pos[i] - p)
    result.append(dist)

min_index = result.index(min(result))
print(pos[min_index])

# 교재 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

## 중간값(median)을 출력
print(data[(n - 1) // 2])

# 느낀점
"""
해당 문제의 핵심 아이디어가 정확히 중간값에 해당하는 위치에 안테나를 설치했을 때
안테나로부터 모든 집까지의 거리가 총합이 최소가 된다는 것인데 문제를 풀때는 전혀
생각하지 못했고, 해설을 읽고나서도 직관적으로 와닿지 않아
1 2 3 108 109 600을 예시로 돌려봤는데 정말로 중간값이 총합이 최소인 결과가 나오게
되었다. 
"""
