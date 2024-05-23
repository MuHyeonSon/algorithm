# for문 풀이

def solution(phone_book):
    answer = True
    phone_book.sort()
    #for i in range(10):
    for i in range(0, len(phone_book)-1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True

# startswith 풀이
'''
def solution(phone_book):
    answer = True
    phone_book.sort()
    #for i in range(10):
    for i in range(0, len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
'''
