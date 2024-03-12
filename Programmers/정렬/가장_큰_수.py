# 정수를 이어 붙여 만들 수 있는 가장 큰 수는
def solution(numbers):
    answer = ''
    numbers = [str(s) for s in numbers]
    numbers.sort(key=lambda x : x * 3, reverse=True) # 자리수 적은 숫자를 반복시켜서 비교 가능하게 만듬
    answer = ''.join(numbers)
    answer = int(answer)
    return str(int(answer)) # 0000 => 0으로 만들기 위해 int처리

'''
https://school.programmers.co.kr/learn/courses/30/lessons/42746
느낀점 :
str type으로 만든 뒤 정렬을 시킴으로써 34보다 9가 더 큰 수로 취급할 수 있도록 만들 수 있었다.
하지만 3과 30에서 3을 더 큰 수로보고 3을 앞으로 위치시킬 수 있게하는 부분에서 막혔다.
key=lambda x: [-int(x[0]), -int(x[1]), -int(x[2])] 조건으로 앞자리부터 차례로 비교하고자 했으나 자리수가
더 작은수는 index out of range 에러가 발생하여 실패하였다.
위와 같이 자리수가 더 작은 수를 임의로 더 큰 자리수에 숫자로 만들어 3과 30에서 3이 더 앞에 오도록 만들 수 있었는데
x : x * 3 식을 키로 사용하게 되면 30과 3을 비교할 때 303030과 333을 비교하게 되고 333이 303030보다 앞에 위치되도록
정렬이 되어서 결론적으로 3이 30보다 더 앞에 정렬될 수 있게 된다. 이 방법을 꼭 기억하자.
'''
