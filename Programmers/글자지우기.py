# 하나씩 없애기 => 인덱스 정보 손상됨
# 한 번에 없애기 => 안 됨
# 하나씩 없애면서 인덱스 정보를 보존하는 방법
# 인덱스 문자열만 제외하고 뽑아오는 거야

def solution(my_string, indices):
    result = ''
    for i in range(len(my_string)):
        if i not in indices:
            result += my_string[i]
    return result
