"""
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.

예를 들어 d(91) = 9 + 1 + 91 = 101 이 때, n을 d(n)의 제네레이터(generator)라고 한다.

위의 예에서 91은 101의 제네레이터이다.

어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.

그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.

예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다. 

시작 값(a)과 마지막 값(b)가 입력되면 두 수 사이의 셀프 넘버들의 합을 출력하시오.

입력
시작 값(a)과 마지막 값(b)이 공백으로 분리되어 입력된다.( 1 <= a <= b <= 5,000)

출력
두 수사이의 셀프넘버들의 합을 출력한다.

입력 예시   
1 10

출력 예시
25

도움말
1부터 10사이의 셀프 넘버는 1, 3, 5, 7, 9이다. 

따라서 합은 25
"""

def whose_generator(nn):
  sum_ = 0
  for x in str(nn):
    sum_ += int(x)
  sum_ += int(nn)

  return sum_

a, b = map(int,input().split())

num = []
for i in range(b+1):
  num.append(i)

for i in range(b+1):
  if a <= whose_generator(i) <= b: # 이 방식으로 사용하면 뒤에 경우까지 다 볼 수 없음 그냥 a부터 b까지 다 제너레이터에 넣어 봐야됨
    num[whose_generator(i)] = 0


print(sum(num[a:b+1]))

#refernece : https://silverhat-diary.tistory.com/4
