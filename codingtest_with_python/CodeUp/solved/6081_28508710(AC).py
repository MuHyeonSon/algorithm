"""
B
출력 예시
B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5

"""

n = input()
n_h = int(n,16)


for i in range(1,16):
    print(n+"*"+'%X'%(i)+"="+'%X'%(n_h*i))
