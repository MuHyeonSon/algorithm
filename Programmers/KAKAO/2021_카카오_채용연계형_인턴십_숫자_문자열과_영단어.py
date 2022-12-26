# 2021_카카오_채용연계형_인턴십_숫자_문자열과_영단어.py

# 나의 풀이
def solution(s):
    # 영단어 표에 대한 dictionary 정의
    number_englishword_dictionary = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3,
                                    "four" : 4, "five" : 5, "six" : 6, "seven" : 7,
                                    "eight" : 8, "nine" : 9}
    temp_s = "" # 딕셔너리에 있는 단어를 찾기 위한 임시 문자열 정의
    result = "" # 원래 숫자에 대한 문자열을 저장할 변수
    # 문자열 찾기
    for charactor in s:
        # 만약 해당 문자가 숫자라면
        if charactor.isdigit():
            result += charactor # 최종 반환 숫자에 concatenate
        # 숫자가 아니라면
        else :
            temp_s += charactor # 임시 문자열에 concatenate
            # 하나씩 읽어들인 후 모아진 문자열이 대응되는 숫자가 있다면
            if temp_s in number_englishword_dictionary :
                result += str(number_englishword_dictionary[temp_s]) # 대응되는 숫자를 최종 반환 숫자에 concatenate
                temp_s = "" # 하나의 문자열이 숫자로 대응되었으니 초기화         
    answer = int(result) # 최종 반환 숫자를 정수형으로 변환
    return answer

# 다른 사람의 풀이 방법 적용 (replace 적용, items() 적용)

def solution(s):
    # 영단어 표에 대한 dictionary 정의
    number_englishword_dictionary = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3,
                                    "four" : 4, "five" : 5, "six" : 6, "seven" : 7,
                                    "eight" : 8, "nine" : 9}
    for key, value in number_englishword_dictionary.items():
        s = s.replace(key,str(value))
    """
    temp_s = "" # 딕셔너리에 있는 단어를 찾기 위한 임시 문자열 정의
    result = "" # 원래 숫자에 대한 문자열을 저장할 변수
    # 문자열 찾기
    for charactor in s:
        # 만약 해당 문자가 숫자라면
        if charactor.isdigit():
            result += charactor # 최종 반환 숫자에 concatenate
        # 숫자가 아니라면
        else :
            temp_s += charactor # 임시 문자열에 concatenate
            # 하나씩 읽어들인 후 모아진 문자열이 대응되는 숫자가 있다면
            if temp_s in number_englishword_dictionary :
                result += str(number_englishword_dictionary[temp_s]) # 대응되는 숫자를 최종 반환 숫자에 concatenate
                temp_s = "" # 하나의 문자열이 숫자로 대응되었으니 초기화
    """
    answer = int(s) # 최종 반환 숫자를 정수형으로 변환
    return answer


# 42 분 21 : 42 초 

# 느낀점
"""
새벽에 풀었다지만 너무 푸는 속도가 느리다는 것을 느꼈고, 딕셔너리 사용도 많은 부분을 까먹었다는 것을 느낄 수 있었다. 
"in"을 사용할 때 key를 기준으로 찾는 다는 것을 확실하게 알게 되었다. 지금 다른 분들의 풀이를 보니 너무 나도 간단한 문제라는 것을 알게되었다.
그냥 단순하게 replace하면 되는 문제였다. 내가 알지 못했던 것은 replace를 문자 하나가 아닌 문자열에 대해서도 적용할 수 있다는 것이고
그렇게 하였을 때 저런 조건문을 사용할 필요없이 반복문 하나면 끝나는 것이었다. 또한 딕셔너리를 사용할 필요도 없었다.
하지만 여기까지는 생각하기 힘들었을 것 같다. 그렇다해도 딕셔너리를 사용하면 반복문 하나로 처리가 가능한 문제였고, 여기서 딕셔너리의 key, value 쌍을 튜플 형태로 얻는
.items() 를 이용하여 더 간단하게 구현할 수 있었다. 
"""
