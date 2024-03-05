n, m = map(int, input().split()) # 세로 (row), 가로 (column)

ice_templet = []

for _ in range(n):
    row = list(input())
    row = [int(s) for s in row]
    ice_templet.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]

print(f'visited : \n{visited}')
print(f'ice_templet : \n{ice_templet}')


# 상하좌우 방향 벡터
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0

# 모든 위치(0인곳이면서 아직 방문하지 않은 곳)에서 커넥티드 컴퍼넌트를 확인하자
def dfs(ice_templet, v, visited):
    visited[v[0]][v[1]] = True
    #print(v[0], v[1], end='\n')
    for i in range(4):
        r_ = v[0] + dr[i]
        c_ = v[1] + dc[i]
        if (0 <= r_ < n) and (0 <= c_ < m):
            #print(f'r_, c_ : {r_}, {c_}')
            #print(f'visited : {visited}')
            #print(f'visited[{r_}][{c_}] : {visited[r_][c_]}')
            #print(f'ice_templet[{r_}][{c_}] : {ice_templet[r_][c_]}')
            if (not visited[r_][c_]) and (ice_templet[r_][c_] == 0):
                dfs(ice_templet, [r_,c_], visited)
            
for i in range(n):
    for j in range(m):
        if (not visited[i][j]) and (ice_templet[i][j] == 0):
            #print("=" * 100)
            dfs(ice_templet, [i, j], visited)
            result += 1

print(result)


# connected_component 찾는 문제 => DFS 사용



# 생각해볼점
"""
계속 헤맨점 : visited를 얕은 복사(shallow copy)를 하여 만들었기 때문에 visited[0][0]만 변경하였음에도 모든 행의 첫번째 열이 True로 변경되었다.
visited = [[False] * m]*n (X)
visited = [[False for _ in range(m)] for _ in range(n)] (O)

원인
visited = [[False] * m]*n 에서 [False] * m은 원소가 모두 False인 리스트를 m개 만들지만, *n 부분에서는 이 리스트를 n번 참조하는 새로운 리스트를 만든다. 
즉, 이렇게 생성된 리스트의 각 행은 모두 같은 객체를 참조하게 된다.
따라서 visited[0][0] = True와 같이 한 행의 값을 변경하면, 같은 객체를 참조하고 있는 모든 행의 값이 함께 변경되게 된다.


 파이썬에서 리스트를 복사할 때, 단순히 =을 사용하면 얕은 복사(shallow copy)가 이루어진다. 이 경우, 복사된 리스트는 원본 리스트와 같은 객체를 참조하기 때문에 원본 리스트를 변경하면 복사된 리스트도 같이 변경됩니다.

따라서 visited 리스트를 생성할 때, 같은 리스트를 여러 번 참조하도록 만들었다면, visited[0][0] = True를 수행할 때 모든 행의 첫 번째 열이 True로 변경되는 것이다.

이를 해결하려면, 파이썬의 깊은 복사(deep copy) 기능을 사용하거나, 리스트를 생성할 때 각 행을 별도의 리스트로 만들어야 한다
visited = [[False for _ in range(m)] for _ in range(n)]

# 그냥 이동이 방문처리를 1로 해버리고 이동이 가능한 경우를 원소값이 0인 것으로하자 (너무 복잡하게 작성했다)

dx, dy 방향벡터 만들지 않아도 되고, graph를 넘겨줄 필요도 없다
dfs(row, column)하고 dfs(row-1, column), dfs(row, column+1) 과 같은 방식으로 됨
"""
