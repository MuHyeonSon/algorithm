# 문자열 압축

def solution(s):
    shortest = len(s)
    for length in range(1, (len(s) // 2) + 1): # 최대한 줄일 수 있는 건 절반임(반복되어야하니까)
        temp_s = ''
        window_s = s[:length]
        count = 1
        for j in range(length, len(s), length): # 윈도우 슬라이딩
            if window_s == s[j:j+length]: # 이전 윈도우가 현재 윈도우와 같다면
                count += 1 # count 증가
            elif count > 1 and window_s != s[j:j+length]:
                temp_s += f'{count}{window_s}'
                window_s = s[j:j+length]
                count = 1
            else:
                temp_s += window_s
                window_s = s[j:j+length]
        temp_s += f'{count}{window_s}' if count >= 2 else window_s
        shortest = min(shortest, len(temp_s))      
    return shortest

# 제한시간 30분, 풀이시간 : 대략 2시간 40분

'''
생각해볼점
a = "aabbaccc" # 길이 : 8, 최대인덱스 :7
b = [1,3,2] # 길이 : 3, 최대인덱스 :2
print(a[100:400]) # 실행결과 : ''
print(b[100:400]) # 실행결과 : []
# 인덱싱할 때는 위아래 상관없이 범위 초과해도 에러가 발생하지 않음
'''

''' 1차 풀이
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
'''
