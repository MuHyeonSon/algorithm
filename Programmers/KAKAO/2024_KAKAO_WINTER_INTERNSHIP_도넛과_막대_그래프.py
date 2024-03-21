def solution(edges):
    answer = [0,0,0,0]
    node_dict = dict()
    for edge in edges:
        source = edge[0]
        target = edge[1]
        if not node_dict.get(source):
            node_dict[source] = [0, 0] # [나간횟수, 받은횟수]
        if not node_dict.get(target):
            node_dict[target] = [0, 0]
        node_dict[source][0] += 1
        node_dict[target][1] += 1
        
    for key, value in node_dict.items():
        out_count = value[0]
        in_count = value[1]
        if out_count >= 2 and in_count == 0:
            answer[0] = key  # 정점의 번호
        if out_count == 0 and in_count > 0: # 막대 모양 그래프 수
            answer[2] += 1
        if out_count >= 2 and in_count >= 2: # 들어온 2개 이상, 나간애 2개이상이면 팔자그래프 개수 1개
            answer[3] += 1
    answer[1] = node_dict[answer[0]][0] - (answer[2] + answer[3]) #도넛=정점의 나간 횟수-(막대+8자) 
    return answer

'''느낀점 or 생각할점
dictionary를 이용하여 풀었고, 모든 그래프를 잇는 정점의 간선 개수를 파악함으로써 전체 그래프 개수를 파악할 수 있었다.
나머지 모든 노드들에 대해서 나가는 간선 수와 들어오는 간선 수를 모두 기록한 뒤, 하나의 그래프에는 반드시 도넛,막대,팔자 각각이 갖고있는
간선의 특징을 보유하고 있는 노드가 있다 따라서 그 노드를 찾아내어 개수를 카운트하면 되는 문제였다.
반드시 다시 풀어보고 이런 연습 및 복습만이 살 길이다.
'''
