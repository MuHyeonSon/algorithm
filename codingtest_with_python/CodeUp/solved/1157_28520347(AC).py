﻿"""
슬기는 체육 선생님과 공던지기로 아이스크림 내기를 하게 됐다.

공을 던져서 50m ~ 60m 사이에 공이 들어가면 슬기가 이기게 되고, 그 외에 공이 떨어지면 체육선생님이 이기게 룰을 정했다.

슬기가 던진 공의 위치가 입력으로 주어지면 50이상 60이하이면 "win"을 출력하고, 그 외에는 "lose"를 출력하시오.

입력
슬기가 던진 공의 위치가 입력으로 주어진다.(실수)

출력
50이상 60이하이면 win을 출력, 그 외에는 lose를 출력하시오.

입력 예시   
50.213

출력 예시
win
"""
height = float(input())
if (height >= 50) and (height <= 60) :
    print("win")
else:
    print("lose")

