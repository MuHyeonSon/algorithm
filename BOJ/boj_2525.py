#boj 2525

h,m = map(int,input().split())
c = int(input())
m = c + m
M = m
if m > 59:
    m = m % 60
    h = h + (M//60)
if h > 23:
    h = h % 24
print(h,m)
