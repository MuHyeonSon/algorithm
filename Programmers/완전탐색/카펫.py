def solution(brown, yellow):
    # 완전탐색 문제
    # 노란색은 중앙에 칠해져있고, 갈색인 테투리는 1줄임
    # brown : 갈색 격자의 수 # yellow는 노란색 격자의수
    # 카펫의 가로, 세로 크기를 순서대로 담아라
    
    # 세로 길이
    for i in range(3, brown // 2): # 세로 길이는 3이상이고, 테두리의 절반의 개수를 절대 넘을 수 없으니까
        # 가로 길이
        for j in range(3, brown // 2): # 가로 길이도 3이상이고, 테두리의 절반의 개수를 절대 넘을 수 없으니까
            # 만약 세로 * 가로 결과와 총 칸의 개수가 같고, 해당 형태가 입력된 테두리 개수와 일치하면
            if i * j == brown + yellow and ((j*2)+(2*(i-2))) == brown:
                answer = [j,i] # [가로, 세로] 출력
                return answer
            
