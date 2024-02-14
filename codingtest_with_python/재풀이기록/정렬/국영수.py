# 국영수 2차 풀이

# 국어 점수가 감소하는 순서로(내림차순)
# 국어점수가 같으면 영어 점수가 증가하는 순(오름차순)
# 국어점수와 영어점수가 같으면 수학 점수가 감소하는 순(내림차순)
# 모든 점수가 같으면 이름 사전 순으로 증가하는 순(오름차순)


n =  int(input())
scores = []
for _ in range(n):
    scores.append(list(map(str, input().split())))

scores.sort(key=lambda x : x[0], reverse=False)
scores.sort(key=lambda x : x[3], reverse=True)
scores.sort(key=lambda x : x[2], reverse=False)
scores.sort(key=lambda x : x[1], reverse=True)

# 결과 출력
for score in scores:
    print(score[0])


# 제한시간 : 20분, 풀이시간 : 15분
# 느낀점
"""
파이썬 정렬함수를 사용할 때, key에 lambda함수에 여러 조건을 한 번에 추가하여, 여러 조건들을 우선순위를 두어 설정할 수 있다는 것을 기억했지만,
막상 떠오르지 않아서 사용하지 못했다. 다음에 풀때는 반드시 기억하고서 사용해보겠다.
"""
