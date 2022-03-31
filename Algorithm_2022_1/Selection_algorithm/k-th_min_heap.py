# 3주차 과제 정답 코드

import heapq

# O(klogk) time algorithm
def solve(A, k):
	cand_min_heap = []
	cand_min_heap.append((A[0], 0))
	for i in range(k):
		cand_idx = cand_min_heap[0][1] # idx of current min value
		result = heapq.heappop(cand_min_heap)[0] # i-th min value
		left_child_idx = 2*cand_idx + 1
		if left_child_idx < len(A):
			heapq.heappush(cand_min_heap, (A[left_child_idx], left_child_idx))
		right_child_idx = 2*cand_idx + 2
		if right_child_idx < len(A):
			heapq.heappush(cand_min_heap, (A[right_child_id])
