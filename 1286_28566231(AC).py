"""
5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성하라.

입력
5개의 정수가 한 줄에 하나씩 입력된다.(범위 : −1,000,000 ~ 1,000,000)

출력
첫째줄에 최댓값을 출력한다.

둘째줄에 최솟값을 출력한다.

입력 예시   
3
7
-4
-6
5

출력 예시
7
-6
"""
temp_list = []
for i in range(5):
    temp_list.append(int(input()))

print(max(temp_list))
print(min(temp_list))
    
