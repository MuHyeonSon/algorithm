def solution(operations):
    import heapq
    q = [] # 우선순위큐로 사용할 리스트 선언
    for operation in operations:
        oper, number = operation.split()
        # 해당 연산이면 큐에 주어진 숫자 삽입
        if oper == "I":      
            heapq.heappush(q, int(number))
        elif oper == "D":
            # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우 무시
            if len(q) == 0:
                continue
            # 해당 연산이면 큐에서 최댓값을 삭제 (최댓값이 둘 이상인 경우 하나만 삭제)
            if number == "1":
                q.pop()
            # 해당 연산이면 큐에서 최솟값을 삭제 (최솟값이 둘 이상인 경우 하나만 삭제)
            elif number == "-1":
                heapq.heappop(q)
    # 모든 연산을 처리한 후 큐가 비어있으면 [0, 0] 반환
    if len(q) == 0:
        answer = [0, 0] 
        return answer
    # 모든 연산을 처리한 후 큐가 비어있지 않으면 [최댓값, 최솟값] 반환
    else:
        answer = [max(q), min(q)] # 이 코드를 우선순위큐쓰니까 [q[-1], q[0]] 이라고 했더니 계속 틀림 결국 이렇게 고치니까 해결됨
        return answer
