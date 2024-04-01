# 모든 달은 28일까지 있다고 가정
# 오늘 날짜 : today
# 약관의 유효기간을 담은 1차원 문자열 배열 : terms
# 개인정보의 정보를 담은 1차원 문자열 배열 : privacies
# 파기해야할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

'''느낀점 or 생각할점
아이디어 자체는 떠올리기 쉽지만,이를 실수없이 빠른 시간 내에 구현해야되는 전형적인 구현 문제였다.
훨씬 더 빨리 풀어야하지만 날짜 계산에 있어 틀린 부분을 찾는데 시간이 많이 소요되었기 때문에 이와 비슷한 구현 문제를 연습하여 빨리 푸는 연습이 필요하다.
또한 유효기간이 지나 파기해야되는지를 구하는 함수를 따로 정의하였는데, 수집날짜로부터 개인정보를 파기하지 않아도 되는 기간까지의 날짜를 구한 뒤, 그 기간이
현재 날짜를 넘었다면 False를, 넘지않았다면 True를 return 하도록 구현했다. 아쉬운 점은 날짜를 구하고 비교하는 기능의 코드가 너무 길어서 가독성이 안 좋았다는 것이다.
만약 코딩테스트를 볼 때 이러한 상황이라면 일단 떠오르는데로 빠르게 구현하는 것이 더 유리할 수도 있겠지만, 
이것이 실무를 할 때의 개발해야된다면 반드시 이것보다 더 간단하고, 가독성 좋도록 코드를 작성해야될 것이다.
'''

def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    for term in terms:
        kind, valid_period = term.split(" ") 
        terms_dict[kind] = int(valid_period)
    for i in range(len(privacies)):
        collected_date, kind = privacies[i].split(" ")
        valid_period = terms_dict[kind]
        if not check_over(collected_date, today, valid_period):
            answer.append(i+1)
    return answer

def check_over(collected_date, now, valid_period):
    c_year, c_month, c_date = map(int, collected_date.split("."))
    n_year, n_month, n_date = map(int, now.split("."))
    l_year, l_month, l_date = 0, 0, 0
    days_valid_period = (valid_period * 28) - 1 # 한달은 무조건 28일이라고 했으니(전날까지유효하므로 -1)
    l_date = c_date + days_valid_period
    # 유효한 마지막 날짜 계산 및 현재 날짜와 비교
    if l_date <= 28:
        l_month = c_month
    else:
        if l_date % 28 == 0:
            l_month = c_month + (l_date // 28) - 1
            l_date = 28
        else:
            l_month = c_month + l_date // 28
            l_date = l_date % 28
    if l_month <= 12:
        l_year = c_year
    else:
        if l_month % 12 == 0:
            l_year = c_year + (l_month // 12) - 1
            l_month = 12
        else:
            l_year = c_year + (l_month // 12)
            l_month = l_month % 12
    if n_year > l_year:
        return False
    elif n_year < l_year:
        return True
    if n_month > l_month:
        return False
    elif n_month < l_month:
        return True
    if n_date > l_date:
        return False
    else:
        return True
        
    
