#부스트캠프_부스트캠프 웹·모바일 6기_자가진단문제_6

# 함수 구현
# 자연수가 들어있는 배열 arr가 매개변수로 주어집니다.
# 배열 arr안의 숫자들 중에서 앞에 있는 숫자들부터 뒤에 중복되어 나타나는 숫자들 중복 횟수
#를 계산해서 배열로 return 하도록 solution 함수를 완성해주세요
# 만약 중복되는 숫자가 없다면 배열에 -1을 채워서 return 하세요.

def al(arr):
  if (len(arr) <= 100 and len(arr) >=1):
    for i in arr:
      if i <=100 and i >= 1:
        continue
      else : break
      
    arr.sort()
    #print(arr)
    an = []
    o = 0
    for i in range(len(arr)):
      count = 0
      #print(f'an : {an}')
      if arr[i] == o : continue
      for j in range(1,len(arr)):
        #print(f'i : {i}, j : {j} ')
        #print(arr[i] == arr[j])
        #print(f'arr[i] != o and arr[i] == arr[j] : {arr[i] != o and arr[i] == arr[j]}')
        #print(f'arr[{i}] : {arr[i]}, arr[{j}] : {arr[j]} ')
        if arr[i] == arr[j]:
          o = arr[i]
          #print(f'o : {o}')
          count += 1
          #print(f'count:{count}')
          #print(f'len(arr) : {len(arr)}')
          #print("\n")
          #print("@@@@@@@@@@@@")
          #print(f'j : {j}, (len(arr)-1) : {(len(arr) -1)}')
          #print(f'j == (len(arr) - 1):{j == (len(arr) - 1)}')
          #print("@@@@@@@@@@@@")
          #print("\n")
        if j == (len(arr) - 1):
          if count != 0:
              an.append(count)
    if len(an) == 0 : return [-1]
    elif len(an) != 0 : return an
    

arr = [4,5,6,4,4,5,6,2,4]
print(al(arr))