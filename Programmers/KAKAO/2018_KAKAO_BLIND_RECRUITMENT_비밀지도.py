# 2018_KAKAO_BLIND_RECRUITMENT_비밀지도.py

# 나의 풀이 (44분 37초 85초 걸림)
def solution(n, arr1, arr2):
    answer = []
    # 이진수를 5자로 표현해야됨
    for index in range(n):
        one_row = ""
        # 지도 1과 지도 2에서 모두 공백인 부분이라면
        arr1_binary = f'{arr1[index]:0{n}b}' ## 이진수로 변환하고 5개 길이의 문자열로 반환하되 숫자외 나머지 글자들은 0으로 채움
        arr2_binary = f'{arr2[index]:0{n}b}'
        print(f'arr1_binary: {arr1_binary}')
        print(f'arr2_binary: {arr2_binary}')
        for index_of_binary_number in range(n):
            if arr1_binary[index_of_binary_number] == "0" and arr2_binary[index_of_binary_number] == "0":
                #answer[n][index_of_binary_number] += " "
                one_row += " "
            else :
                #answer[n][index_of_binary_number] += "#"
                one_row += "#"
        answer.append(one_row)
    return answer
  
  # 입력을 사용자에게 받는게 아니라 그냥 함수만 완성하는 건가?
#n = int(input()) # 지도의 한 변의 길이(정사각형 배열)
#arr1 = list(map(int,input().split()))
#arr2 = list(map(int,input().split()))
#print(solution(n,arr1,arr2))
  
# 나의 풀이 (최종 코드)

def solution(n, arr1, arr2):
    answer = [] # 전체지도
    for index in range(n):
        one_row = ""
        arr1_binary = f'{arr1[index]:0{n}b}'
        arr2_binary = f'{arr2[index]:0{n}b}'
        print(f'arr1_binary: {arr1_binary}')
        print(f'arr2_binary: {arr2_binary}')
        for index_of_binary_number in range(n):
          # 지도 1과 지도 2에서 모두 공백인 부분이라면 공백
          if arr1_binary[index_of_binary_number] == "0" and arr2_binary[index_of_binary_number] == "0":
            one_row += " "
          # 어느 하나라도 벽인 부분이라면 벽
          else :
            one_row += "#"
        answer.append(one_row)
    return answer
  
  
  # 나의 풀이 (bitwise 연산 적용, replace로 값 변경)

  def solution(n, arr1, arr2):
      answer = [] # 전체지도
      for index in range(n):
          one_row = ""
          one_row = f'{arr1[index] | arr2[index]:0{n}b}'
          one_row = one_row.replace("1", "#") # replace는 값이 변경되지 않음!
          one_row = one_row.replace("0", " ")

          answer.append(one_row)
      return answer
  
  
# 해설
"""
이 문제는 비트 연산Bitwise Operation을 묻는 문제이고. 이미 문제 예시에 2진수로 처리하는 힌트가 포함되어 있고, 둘 중 하나가 1일 경우에 벽 #이 생기기 때문에 OR로 처리하면 간단히 풀 수 있습니다.
아주 쉬운 문제였던 만큼 if else로 풀이한 분들도 많이 발견되었습니다. 정답으로는 간주되지만 이 문제는 비트 연산을 잘 다룰 수 있는지를 묻고자 하는 의도였던 만큼 앞으로 이런 유형의 문제를 풀 때는
비트 연산을 꼭 기억하시기 바랍니다.

정답률은 81.78% .
""
  
  
# 느낀점
  """ 너무 오래걸리고 입력을 직접입력하지 않는 것인지 헷갈려 초반에 헤맴,
     이진수로 변경하고 그 2진수를 원하는 형식에 맞추어 포맷팅하는 것을 제대로 알지 못했음
    실제 코테에서 오픈북이 아니므로 몰랐다면 아예 못풀었을 수 있으니 절대 까먹지 말아야 겠다고 생각했다.
    
    하지만 해설을 보니 이문제가 if-else로 처리하는 것이 아닌 "비트 연산Bitwise Operation을 묻는 문제" 였다.
    따라서 OR로 처리하면 매우 간단하게 해결이 되었던 문제이고, 해설에서 말씀해주신 것처럼 
    향후 이러한 문제를 만나게 되면 비트 연산을 잘 다룰 수 있는지를 묻고자 하는 의도라는 것을 파악하고 앞으로 이런 유형의 문제를 풀 때는
비트 연산을 꼭 기억해야겠다고 생각했다.
업무에서 있을만한 상황을 가정하여 독창적이고 다양한 분야의 문제를 출제한 것이라고 하였으니 비트 연산Bitwise Operation에 대해
기억하고 있어야 한다. 또한 다른 유저들의 풀이를 보니 한 줄로 짠 코드도 있었고, rjust replace 등을 적용하여 
훨씬 더 효율적으로 코드를 작성했음을 알 수 있었다. 나의 풀이와 다른 사람의 코드를 비교해보며 도움을 얻는 것에
중요성을 다시 한 번 느낄 수 있었다.
    
    """
  
 
