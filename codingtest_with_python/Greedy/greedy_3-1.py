# condingtest_with_python_part2_greedy

# example 3-1 거스름 돈

# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야할 동전의 최소 개수를 구하라.

n = 1260 # 거슬러줘야 할 돈 1260원
count = 0 # 동전의 개수

# 큰 단위 화폐로부터 차례대로 확인
coin_types = [500,100,50,10]

for coin in coin_types:
  count += (n // coin) # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin

print(count)
  
