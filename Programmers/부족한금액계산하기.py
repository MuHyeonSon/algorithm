def solution(price, money, count):
    total = 0 #놀이기구 count번 타는데 필요한 비용저장할 변수
    for i in range(1, count + 1):
        total += price * i
    answer = money - total
    # 금액이 부족한 경우 부족한 금액을 양수로 출력하기 위해 -1 곱해줌
    if answer < 0:
        answer = answer * -1
    # 금액이 부족하지 않은 경우 0 return
    else:
        return 0
    return answer
