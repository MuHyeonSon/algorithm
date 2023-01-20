# condingtest_with_python_part3_구현
# 자물쇠와열쇠.py



# 나의 풀이 (교재 해설 참고)

## 90도 회전하는 함수
def rotate(matrix):
    n = len(matrix) # 입력 행렬의 row 크기
    m = len(matrix[0]) # 입력 행렬의 column 크기
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result

## lock에 key를 더한 결과 중앙이 모두 1인지 확인하는 함수
def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True
            
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)] # 자물쇠의 크기를 기존의 3배로 변환(완전탐색할 때, 계산수월하게 하도록)
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    # 네가지 각도(네가지 방향)에서 전부 확인해보기
    for _ in range(4):
        key = rotate(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 자물쇠에 대해 열쇠가 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠다시빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 못품)
"""
열쇠는 회전과 이동이 가능
이동은?? 
afine tansfome 쓰면 되지 않아?? rotate랑, transition

자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향 안 줌
자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물소의 홈부분이 정확히 일치해야되고 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨
자물쇠의 모든 홈을 채워 비어있는 곳이 없도록 해야 자물 쇠 열 수 있음

완전탐색으로 \?? 만약 그렇게 하면 90도 간격으로 회전하여 4경우의 각도에 대해 각각 모든 이동경우 다 구해야됨(
만약 3x3 행렬이면, x축 방향으로 -2~2, y축 방향으로 -2~2를 더하는 경우를 모두 탐색해봐야됨 그중 하나라도
모든 원소의 합이 N*N이라는(3x3행렬일 경우 모든 원소 다 더하면 9니까)숫자가 나온다면 True를 리턴하자)

문제는 rotate야 rotate 행렬 어떻게 만들더라?? cos sin 넣어야 되는 걸로 기억하는데 
 cosx -sinx   0
 sinx  cosx   0
 0      0     1
 꼬마신신꼬?
 만약 입출력예 key에다가 x에 90넣고 곱해보면
 0   -1
 1    0
 근데 생각해보니 문제는 20x20까지 있음 회전 변환 행렬 만들기 힘듬.. 
 행렬곱 연산 파이썬에서 지원하나?? 일단 모르겠음 지금은
 시계방향으로 90도 회전했을 때 key의 세 개의 돌기의 위치 변화
 2,1 -> 1,2   3,2 -> 2,1  3,3 -> 3,1
"""




# 느낀점
"""
90도 회전하는 함수 어떻게 구현해야되는지 계속해서 생각해봤지만 결국에 찾지 못하여
해설을 보고 풀 수 있었다.
핵심은 두 가지였다.

1. 완전탐색을 이용하고 완전탐색을 수월하게 하기 위해 리스트를 자물쇠리스트를 row column 모두 3배를 늘린 리스트를 만들고 중앙에 자물쇠를 위치시킨다.
    => 그렇게 하면 transitation과 rotate 둘 다 수원할게 계산이 가능하다 .
2. 2차원 리스트를 90도 회전한 결과를 반환하는 함수 구현 방법 => 가끔씩 2차원 리스트 다룰 때 사용하므로 노트에 적어두고 필요할 떄 사용해야 된다.

다음에 비슷한 문제를 만나면 무조건 풀어야겠다고 생각했다.
"""
