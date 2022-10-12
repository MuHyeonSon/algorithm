""" 
 두 소 수 의 곱 을 암 호 로 사 용 하 는 알 고 리 즘 은 큰 수 의 소 인 수 분 해 가 어 렵 기 때 문 에 안 전 하 다 고 알 려 져 있 다 . 

 그 렇 지 만 , 만 약 두 소 수 를 잊 어 버 리 면 어 떻 게 될 까 ? 굉 장 히 난 감 할 것 이 다 . 

 이 에 대 비 해 어 떤 수 (n) 가 입 력 되 면 두 소 수 의 곱 으 로 나 타 낼 수 있 으 면 두 소 수 를 오 름 차 순 으 로 출 력 하 고 , 

 그 렇 지 않 으 면 "wrong number" 를 출 력 하 는 프 로 그 램 을 작 성 하 시 오 . 

 입 력 
 어 떤 수 n 이 입 력 된 다 .( 단 , 1&lt;=n&lt;=10,000,000) 

 출 력 
 n 을 두 소 수 의 곱 으 로 나 타 낼 수 있 으 면 두 수 를 오 름 차 순 으 로 출 력 한 다 . 

 ( 단 , 가 능 한 소 수 중 가 장 작 은 소 수 와 의 곱 으 로 나 타 낸 다 .) 

 하 고 , 그 렇 지 않 으 면 "wrong number" 를 출 력 한 다 . 

 입 력 예 시 
 21 

 출 력 예 시 
 3 7 
 """ 

f_list = []

# 소 인 수 분 해 함 수 정 의 

def factorization(x) : 
    d = 2 
    factorization_list = [] 
    while d <= x : 
        if x % d == 0 :
            #print(d) 
            factorization_list.append(d)
            #print(factorization_list) 
            x = x / d 
        else : 
            d = d + 1

    #print(factorization_list)
    #print('----------------------------------') 
    global f_list
    f_list = factorization_list.copy()
n = int(input())
if n == 1:
  print("wrong number")
else:
  factorization(n)
  #print(f_list)

  #f_list = factorization(n)
  #print(len(f_list))
  if len(f_list) % 2 == 0 : 
      f_list.sort() 
      mul = 1 
      for i in range(1,len(f_list)) : 
          mul *= f_list[i] 
          print(int(f_list[0]),int(mul)) 
  else : 
      print("wrong number")
