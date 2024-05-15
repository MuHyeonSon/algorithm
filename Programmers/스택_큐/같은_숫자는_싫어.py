# 숫자를 하나씩 확인, 이전 숫자랑 다르면 answer에 추가

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    temp = -1
    for a in arr:
        if a != temp:
            answer.append(a)
            temp = a
            continue
    return answer
