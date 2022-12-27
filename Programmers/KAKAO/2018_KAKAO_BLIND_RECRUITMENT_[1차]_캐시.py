# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하라
# 출력은 입력된 도시이름 배열을 순서대로 처리할 때, 총 실행시간을 출력
# 캐시 교체 알고리즘은 LRU를 사용함 (이 알고리즘이 무엇인지 알아야 풀 수 있음.)
# * Cache Hit 이란?
# CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우, Cache Hit이라고 한다.
# * Cache Miss란?
# CPU가 참조하고자 하는 메모리가 캐시에 존재하지 않을 떄는 Cache Miss라고 함.
# LRU : 가장 최근에 사용된 적이 없는 캐시의 메모리부터 대체하며 새로운 데이터로 갱신

# 나의 풀이

def solution(cacheSize, cities):
    time = 0
    # 캐시크기가 0이면
    if cacheSize == 0:
        time = 5 * len(cities)
        return time
    # 캐시크기가 0보다 크면
    else :
        cache = [] # 캐시 리스트 선언
        for city in cities :
            city = city.lower() # 대소문자 구분하지 않으므로 소문자로 모두 변환
            # cache hit일 경우
            if city in cache :
                time += 1
                cache.pop(cache.index(city)) # hit에 해당되는 데이터를 뽑아서
                cache.append(city) # 가장 최근에 접근한 위치로 위치시킴

            # cache miss일 경우
            else :
                if len(cache) == cacheSize :
                    time += 5
                    # 가장 최근에 사용된 적이 없는 첫 번째 인덱스 원소를 교체
                    cache.pop(0)
                    cache.append(city)
                # cache가 다 채워지지 않은 초기의 경우
                else :
                    time += 5
                    cache.append(city)
    return time



# 느낀점
"""
아무리 어떤 일이 있었다지만 입출력표를 제대로 읽어보지 않으니
문제에 대해 제대로 이해하지 못하고 에러를 해결하려다보니 엄청나게 시간을 낭비했다..
따라서 입출력 표를 잘 보고 문제를 먼저 정확히 이해하는 태도가 나에게 더 필요하다.

내가 몰랐던 개념 or 잊어버렸던 개념들
1. LRU
2. cache hit
3. cache miss
4. 대소문자 파이썬 메서드 (isupper(),islower(),upper(),lower())

또한 다른 사람의 풀이를 보니 deque 자료구조의 maxlen을 사용하여
아주 간단하게 처리한 것을 알 수 있었다.
"""
