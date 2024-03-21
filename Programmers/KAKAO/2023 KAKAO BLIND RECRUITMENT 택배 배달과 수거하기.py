def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    current_deliveries = 0
    current_pickups = 0
    for i in range(n):
        current_deliveries += deliveries[i]
        current_pickups += pickups[i]
        while current_deliveries > 0 or current_pickups > 0:
            current_deliveries -= cap
            current_pickups -= cap
            answer += (n - i) * 2 # while문안에 있어야 0/0인 경우를 거를 수 있음
    return answer

''' 느낀점 or 생각할 점
처음에는 물류창고에서 애초에 몇개를 가져나와야될지부터 결정하는 코드를 작성해야되지 않을까 했다.
하지만 결국 제일 멀리있는 곳부터 처리하는 것이 가장 최소 거리이며(가장 먼곳을 여러번 더 가게되면 낭비이고, 가는 길에 cap이 충분하면
가는 길에 배달하고 수거할 수도 있기 때문이다) 배달을 마치면 다시 여유공간이 생기기 떄문에 한 차례에 cap을 현재 집에서 배달해야될 양과 픽업해야될양에서
cap을 빼주고 남는 것은 계속 빼준 뒤, 배달할 것과 수거할 것이 전부 0이하이게 되면 그때서 다음집에 방문하면 되는 거였다.
떠올리기는 어렵지만 생각보다 크게 복잡한 문제는 아니었으므로 이런 문제를 쉽게 풀려면 연습과 복습만이 살 길이다.
'''
