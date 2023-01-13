def solution(strings, n):
    #strings.sort()
    #strings.sort(key = lambda x : x[n])
    strings.sort(key = lambda x : (x[n],x))
    return strings
