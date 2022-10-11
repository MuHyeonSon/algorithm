height, weight = map(float,input().split())

if height < 150:
  standard_weight = (height - 100)
elif 150 <= height < 160 :
  standard_weight = (height - 150)/2 + 50
elif height > 160:
  standard_weight = (height - 100) * 0.9

#비만도 = (실제 몸무게 - 표준몸무게)  * 100 / 표준 몸무게
bimando = ((weight - standard_weight) * 100) / standard_weight

if bimando > 20:
    print("비만")
elif 10 < bimando <= 20:
    print("과체중")
elif bimando <= 10:
    print("정상")
