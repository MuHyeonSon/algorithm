# condingtest_with_python_part3_DFS/BFS
# 괄호변환.py

# 나의 풀이 (교재 해설 참고)

## 도대체 어떻게 dfs로 풀어?? 이 문제는 엄연히 dfs/bfs문제는 아니지만,
## 재귀 함수 구현을 요하기 때문에 dfs함수를 구현할 때의 핵심인 재귀함수 구현을 요구하는 문제임

## 균형잡힌 문자열이 올바른 문자열인지 확인하는 함수
def check_corrected(u):
    correct = False
    stack = []
    if u[0] == '(':
        stack.append(u[0])
        for i in range(1, len(u)):
            if u[i] == '(':
                stack.append(u[i])
            elif u[i] == ')':
                stack.pop()
        if len(stack) == 0:
            correct = True
    return correct

## 균형잡힌 문자열의 인덱스를 반환하는 함수
def search_balanced(p):
    for i in range(1, len(p)+1):
        if p[0 : i].count('(') == p[0 : i].count(')'):
            return i

def solution(p):
    answer = ""
    # 1
    if p == "":
        return p
    # 2
    index = search_balanced(p)
    u = p[:index]
    v = p[index:]
    # u가 올바른 괄호 문자열인지 확인
    if check_corrected(u):  
        # 3 만약 u가 올바른 괄호 문자열이라면 v에 대해 1단계 부터 다시 수행
        # 3-1 수행한 결과 문자열을 u에 붙인 후 반환
        u = u + solution(v)
        return u
    # 만약 u가 올바른 괄호 문자열이 아니라면
    else:
        # 4-1
        answer = "("
        # 4-2
        answer = answer + solution(v)
        # 4-3
        answer = answer + ")"
        # 4-4
        u = u[1:]
        u = u[:-1]
        for i in range(len(u)):
            if u[i] == "(":
                u = u[:i] + ")" + u[i+1:]
            elif u[i] == ")":
                u = u[:i] + "(" + u[i+1:]
        answer = answer + u
        # 4-5
        return answer
        



# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 분 초 )



# 느낀점
"""
처음에 이 문제를 어떻게 dfs/bfs로 풀 수 있는지 도무지 아이디어가 떠오르지 않아 해설을 보았다.
이 문제는 엄밀히 말하면 DFS문제는 아니지만 DFS 알고리즘의 핵심이 되는 재귀함수 구현을 요구한다는 점에서 DFS 연습목적의 문제라고 한다.
어쩐지 도무지 떠오르지 않았던 이유가 있었던 것이다.

하지만 온전히 나 스스로 다 풀지 못하였고,
"특정문자열에서 균형잡힌 괄호 문자열의 인덱스를 반환하는 함수"와, "균형잡힌 괄호 문자열이 올바른 괄호 문자열인지 판단하는 함수"를 별도로
구현해야된다는 점을 해설을 통해 알고 풀게 됐다. 결론적으로 정답은 구할 수 있었지만 온전히 내 힘으로 풀지 못했기 때문에 아쉬움이 남는다.

이번에 확실히 짚고 넘어가야 할 점은 다음과 같다.

1. 문자열에 리스트를 씌우면 한 글자 단위씩 원소로 들어간 리스트가 된다. => 난 분명 이걸 시도 했다가 에러가 뜬 기억이 있어서, 시도조차 안했는데
    다시 해보니까 된다... 진짜 왜이런건지 모르겠다. => 내 기억이 왜곡됐거나, 당시에 에러를 제대로 해석 못했을 수도 있다.

2. 리스트와 문자열을 합칠댸는 문자열 += "".join(리스트) 쓰면 된다.


"""
