# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야됨

# n명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹의 수의 최댓값

# 몇명의 모험가는 마을에 남아있어도 됨 (다 안써도 됨)

# 그룹의 개수를 최대화로 하려면 공포도가 낮은 애들을 최대한 뽑고, 높은 애들은 뽑지 않는 식이 좋을 거임
# 일단 공포도가 낮은 순으로 정렬한뒤
# 한 명씩 읽어들인 다음에 그룹이 만들어지면 count하자
# 그러다가 현재 읽어들인 모험가에서 나머지 모험가들로 그룹을 더이상 구성할 수 없으면 반복문 탈출


n = int(input())
mohumga = list(map(int, input().split()))
mohumga.sort()

num_group = 0
inwon = 0
max_gongpodo = 0
for i in mohumga:
    max_gongpodo = max(max_gongpodo, i)
    inwon += 1
    if inwon >= max_gongpodo:
        num_group += 1
        inwon = 0
        max_gongpodo = 0
print(num_group)


## 제한시간 30분, 풀이시간 20분 
'''
짚고 넘어갈 점
sort를 하였다면 굳이 max_gongpodo라는 변수를 선언할 필요가 없으니까 훨씬 더 간단하게 짤 수 있었다
그냥 현재 모험가의 공포도가 현재 그룹의 포함된 모험가의 수(inwon) 보다 같거나 작은지만 보면 됐었다.
'''
