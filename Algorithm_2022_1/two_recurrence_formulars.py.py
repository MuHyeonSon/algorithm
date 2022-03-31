def A(n):
	# n번째 값을 리턴함
	if n == 1:
		return 2
	else :
		return 2*A(n//2) + 3*n
	
def B(n):
	# n번째 값을 리턴함
	if n == 1 :
		return 1
	elif n == 2 :
		return 3
	else :
		return 3*B(n-1) - 2*B(n-2) + 2
	
# 1. 자연수 n 값을 입력 받음
n = int(input())
a, b = A(n), B(n)
print(a, b)