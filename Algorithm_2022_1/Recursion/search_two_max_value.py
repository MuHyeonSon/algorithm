def two_max(A, left, right):
	if right - left == 1:
		if left < right:
			return A[right], A[left]# M = 가장 큰 값, m = 두 번째로 큰 값
		if right < left:
			return A[left], A[right]
		# 주의: 입력에 따라 M과 m이 같을 수도 있다
		# 1. base case
	if left == right: # 범위에 해당하는 값이 하나 뿐일 때
			return A[left], None # 가장 큰 값만 정의되므로, 두 번째 큰 값은 None으로 표시해 리턴
	else:
		mid = (left+right)//2
		L1, L2 = two_max(A,left,mid)# 2. 재귀적으로 left ... mid에 대해 가장 큰 값 L1과 두 번째로 큰 값 L2 계산
		R1, R2 = two_max(A,mid+1,right)# 3. 재귀적으로 mid+1 ... right에 대해 가장 큰 값 R1과 두 번째로 큰 값 R2 계산
		B = [L1,L2,R1,R2]
		M,m = two_max(B,0,len(B)-1)
			# 4. L1, L2, R1, R2로부터 left ... right에 대한 M, m을 계산 
	#   (L2와 R2가 None일 수 있음을 유의)
	# 여기서부터 코드 작성
		
	
	
	return M, m
	
A = list(map(int,input().split()))# n개의 정수를 읽어 A에 저장
M, m = two_max(A, 0, len(A)-1)
print(M, m)

# 아래 물음에 대한 자신의 생각을 주석 형태로 서술하세요~
# Q1: 이 알고리즘의 수행시간 T(n)의 점화식은?
# A1: T(n) = c(2n-1) A를 2등분 하면서 찾아가기 때문에 거기에 다른 기본연산을 더하면 T(n) = T(n/2)+T(N/2)+c 가 되고 계속 해서 전개를 하면 그러한 식이 나올 것이라고 생각했습니다.
#
# Q2: T(n)의 점화식을 전개한 후 Big-O로 표기하면?
# A2: O(n)
#
# Q3: 이 알고리즘의 (최학의 경우의) 비교 횟수를 최대한 정확히 분석해보면
# A3: 최악의 경우의 비교 횟수는 n - log2(n)-2 만큼이 필요합니다.
# 최대값을 위한 비교가 n-1번 필요하고 2번째로 큰 값을 위한 비교가 round수-1번이
# 필요한데 round 수는 log2(n)이기 때문에 최종적으로 필요한 비교횟수는 둘을 더한
# n -log2(n)-2가 필요합니다. 상한과 하한이 같아 최악의 경우도 무조건 필요한 비교 횟수와 같습니다.
