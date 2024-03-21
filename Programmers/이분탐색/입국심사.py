# 입국심사를 기다리는 사람 수 n
# 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하라

#입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
#각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
#심사관은 1명 이상 100,000명 이하입니다.

# 이진탐색 pivot 정하고 현재 보는 수가 pivot보다 작으면 거기 버리고 크거나 같은 쪽만 봄
# 이진탐색의 조건 : 탐색하고자 하는 데이터가 정렬이 되어있어야됨
# 모든 경우의 수를 구해야겠지 1~max_time까지
# left : 1
# right : max_time
# 위와 같이 설정 한 뒤, 중점을 찾는다
# 중점은 right와 left를 합친 것을 2로 나눈 것이다
# target이 중점보다 크면 left를 left + 1로
# target이 중점보다 크면 left를 right - 1로 업데이트

def solution(n, times):
    left_time = 1 # 1초이상은 어차피 반드시 걸리므로
    right_time = max(times) * n # 가장시간오래걸리는 심사관에게만 전부 심사받는 경우
    while left_time <= right_time: # 탐색수행조건
        mid_time = (left_time + right_time) // 2
        num_checked_people = 0
        for time in times:
            num_checked_people += mid_time // time # mid_time동안 모든 심사관이 심사할 수 있는 사람의 수
            if num_checked_people >= n: #심사할 사람의 수보다 크거나 같다면
                break
        if num_checked_people >= n: # 심사받은 사람이 심사받아야될사람보다 많거나 같은 경우
            answer = mid_time
            right_time = mid_time - 1
        elif num_checked_people < n: # 심사받은 사람이 심사받아야될사람보다적은경우
            left_time = mid_time + 1
        
    return answer

'''생각할점 or 느낀점
이분탐색의 개념과 동작방법은 떠올릴 수 있었으나, 어떤 데이터로부터 어떤 수를 탐색해야되는지에 대한 아이디어가 잘 떠오르지 않았다.
1부터 가장오래걸리는 심사관이 모든 사람을 심사할 때 걸리는 수를 데이터로 두고 그 중에 최솟값을 탐색하는 것이었다.
현재 mid에 해당하는 시간까지 심사관이 심사할 수 있는 수를 구하는 식으로 풀 수 있다는 것이 잘 이해가 가지않았다.
느낌적으로 모든 심사관이 동일한 비율로 심사를 맡는 것 같기 때문이다. 몇 가지 예시를 한 번 적어보고 잘 와닿지 않더라도 
이 방법이 맞다는 것을 검증하는 것을 빨리 할 수 있도록 해야 될 것 같다.
'''
