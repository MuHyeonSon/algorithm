# condingtest_with_python_part3_구현
# 기둥과보설치.py



# 나의 풀이 (교재 해설 참고)
######## 현재 구조물이 정상인지(제한사항에 걸리는 것이 없는지)체크하는 함수
def check(answer):
    for struct in answer:
        x, y, stuff = struct
        if stuff == 0:
            if y == 0 or [x-1, y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 해당 frame의 작업이 구조물 설치면
        if operate == 1:
            answer.append([x,y,stuff])
            if not check(answer):
                answer.remove([x,y,stuff]) 
        # 해당 frame의 작업이 구조물 삭제면
        elif operate == 0:
            answer.remove([x,y,stuff])
            if not check(answer):
                answer.append([x,y,stuff]) 
            
    return sorted(answer)



# 나의 풀이 (주어진 풀이 시간 : 분, 풀이 시간 : 분 초)
## n : 벽면의 크기, build_frame : 기둥과 보를 설치하거나 삭제하는 작업이 담긴 배열
##           build_frame은 [x,y,a,b] 형태임
##           x,y  : 기둥, 보를 설치 또는 삭제할 교차점의 좌표 x: 가로, y: 세로
##           a는 설치 or 삭제할 구조물의 종류 0 : 기둥 1은 보
##           b는 구조물 설치 or 삭제 여부 , 0 : 삭제 1: 설치
##  최종 구조물의 상태를 return
def solution(n, build_frame):
    result = []
    Map = [[-1] * (n + 1) for _ in range(n + 1)]
    # -1 : 아무것도 없는 칸, 0 : 기둥, 1 : 보
    # 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냄.
    for task in build_frame:
        #x: 가로, y: 세로 a: 0 -> 기둥, 1 -> 보, b: 0 -> 삭제 1-> 설치
        x, y, a, b = task
        if 0 <= x <= n and 0 <= y <= n:
            if a == 0: # 설치 혹은 삭제할 것이 기둥이라면
                if b == 1: # 기둥설치할거라면
                    #기둥이니까 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나,다른 기둥 위에 있다면
                    if y == 0:
                        Map[x][y] = 0
                    elif Map[x-1][y] == 1:
                        Map[x][y] = 0
                    elif Map[x][y-1] == 0:
                        Map[x][y] = 0
                    elif Map[x][y] == 1:
                        Map[x][y] = 0
                    else:
                        continue
                if b == 0: # 기둥삭제할거라면
                    # 기둥 위에 다른 기둥이 있거나 기둥 위아래에 모두 보가 있는 경우, 기둥위에보가있고그보는다른기둥과연결x일때,
                    if y == 0:
                        Map[x][y] = -1
                    elif Map[x-1][y] == 1:
                        Map[x][y] = -1
                    elif Map[x][y-1] == 0:
                        Map[x][y] = -1
                    elif Map[x][y] == 1:
                        Map[x][y] = -1
                    else:
                        continue
            elif a == 1: # 설치 혹은 삭제할 것이 보라면
                if b == 1: #보설치할거라면
                    #보니까 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어 있다면
                    if Map[x][y-1] == 0:
                        Map[x][y] = 1
                    elif Map[x+1][y-1] == 0:
                        Map[x][y] = 1
                    elif (Map[x-1][y] == 1 and Map[x+1][y] == 1):
                        Map[x][y] = 1
                    else:
                        continue
                if b == 0: #보삭제할거라면
                    #보 한쪽 끝위에 기둥이 있거나, 보 왼쪽혹은오른쪽에 보가있고 그밑에 기둥이없다면 삭제x
                    if Map[x][y-1] == 0:
                        Map[x][y] = -1
                    elif Map[x+1][y-1] == 0:
                        Map[x][y] = -1
                    elif (Map[x-1][y] == 1 and Map[x+1][y] == 1):
                        Map[x][y] = -1
                    else:
                        continue
        else:
            continue

    for i in range(n+1):
        for j in range(n+1):
            if Map[i][j] == 0 or Map[i][j] == 1:
                result.append([i, j, Map[i][j]])
    result.sort(key = lambda x : x[2])
    result.sort(key = lambda x : x[1])
    result.sort(key = lambda x : x[0])
    return sorted(result)

#교재풀이
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False # 아니라면 False 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False # 설치된 것이 '기둥'인 경우
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1000개 (제한시간 5초이므로 O(N^3)으로도 가능)
        x, y, stuff, operate = frame
        # 해당 frame의 작업이 구조물 삭제면
        if operate == 0:
            answer.remove([x,y,stuff]) # 일단 삭제를 해본 뒤에
            if not check(answer): # 가능한 구조물인지 확인
                answer.append([x,y,stuff])  #가능한 구조물이 아니라면 다시 설치
        # 해당 frame의 작업이 구조물 설치면
        if operate == 1:
            answer.append([x,y,stuff]) # 일단 설치를 해본 뒤에
            if not check(answer): # 가능한 구조물인지 확인
                answer.remove([x,y,stuff]) #가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환


# 느낀점
"""
1. 처음에 문제를 이해하는 데 시간이 많이소요된 것이 컸고, 

2. 구현했음에도 기둥을 삭제하는 부분에서 제한사항을 먼저 그대로 적어보지 않고
"이렇게도 해야할꺼야"라고 내판단대로 시도하여 더많은 시간을 낭비하였다.
=> 시간이 부족한 코테에서는 이러한 부분은 반드시 고쳐야할 버릇이라고 생각했고,

3.역시나 =을 ==으로 써서 잘못된 경우도 존재했다. => 앞으로도 코드가 실행되지 않으면 이것부터 제일먼저 체크해야겠다.

4. 교재와 내 코드의 다른점은 교재는 한 번 설치 or 삭제를 할 때마다 모든 구조에 이상이 없는 지를 체크하고 진행했지만
나는 그냥 설치할때 그 주변만을 고려하여 코드를 짰다. 결과적으로 테스트케이스는 다 맞았으나 히든 테스트케이스에서 모두 틀려버린 것이다.

5. 또한 나는 2차원 리스트를 사용하여 지도를 통해 확인하는 방법을 사용했으나 문제를 잘 이해했다면 굳이 리스트를 따로 생성할 필요없이
    리스트들 간의 관계만 보면된다는 것을 알게되었다.
    
6. 해설을 보고나서, 풀이방법을 잘 기억한 뒤 구현하였더니 생각보다 너무 간단하게 풀렸다. 구현 문제에 대해 조금 문제가 복잡하게 느껴진다고 해서
겁부터 먹을 필요는 없다고 생각했다. 실제로 코테 풀 때도 분명 풀 수 있을 거라고 생각하면서 중간에 포기만 하지 않으면 그것만으로도
더 좋은 점수를 얻을 수 있을 수 있고, 결과까지 바뀔 수도 있을 거라는 생각을 하게 되었다. 
"""
