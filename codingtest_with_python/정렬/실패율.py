# condingtest_with_python_part3_정렬
# 실패율.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 48분 초 )
def solution(N, stages):
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는
    # 배열을 return하라
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    number_of_player = len(stages)
    lose_rate = [0] * (N + 1)
    for i in range(1, N + 1):
        print(i)
        reach = 0
        clear = 0
        for s in stages:
            if s > i:
                clear += 1
            elif s == i:
                reach += 1  
        if reach == 0 and clear == 0:
            continue
        lose_rate[i] = reach / (reach + clear)
    
    lose_rate.pop(0)

    for i in range(len(lose_rate)):
        lose_rate[i] = (lose_rate[i], i + 1)

    lose_rate.sort(key = lambda x : (-float(x[0]), int(x[1])))
    result = []
    for i in lose_rate:
        result.append(i[1])     

    return result


# 교재 풀이
def solution(N, stages):
    answer = []
    length = len(stages)
    
    # 스테이지 번호를 1부터 N까지 출력
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 살패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
            length -= count
        
        # 리스트에 (스테이지번호, 실패율) 원소 삽입
        answer.append((i, fail))

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t : t[1], reverse = True)

    answer = [i[o] for i in answer]
    return answer


# 느낀점
"""
count 사용과 리스트 컴프리헨션을 통해 더 간단하게 구현하지 못한 것이 아쉬웠다.
"""
