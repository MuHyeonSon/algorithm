#후위 표기 수식 계산 구현 함수
def evalPostfix(expr):
    s = Stack()        #스택 객체 생성
    for token in expr :   #리스트의 모든 원소에 대해
        if token in "+-*/" :  # 항목이 연산자이면
            val2 = s.pop()    #피연산자2
            val1 = s.pop()    #피연산자1
            # 각 연산 수행 결과는 스택에 다시 저장
            if(token == '+'): s.push(val1 + val2)
            elif(token == '-') : s.push(val1 - val2)
            elif(token == '*') : s.push(val1 * val2)
            elif(token == '/') : s.push(val1 / val2)
        else :
            s.push(float(token)) #항목이 피연산자이면 float으로 변경해서 스택에 저장
    return s.pop()  #최종결과를 반환        
    
#중위 -> 후위 변환
def Infix2Postfix(expr): # expr: 입력리스트 (중위표기식)
    s = Stack() #연산자를 집어넣는 용도로 stack 사용
    output = [] #결과를 저장할 리스트(후위표기식)
    for term in expr :
        if term in '(':  #왼쪽괄호이면
            s.push('(')  #스택에 삽입
        elif term in ')': #오른쪽 괄호이면
            while not s.isEmpty(): #Empty인지 체크
                
                op = s.pop()
                if op=='(':break; #왼쪽 괄호가 나올 때 까지
                else: output.append(op)
        elif term in "+-*/" : #연산자이면 우선순위가 높거나 같은 연산자를 스택에서 모두 꺼내 출력
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)): 
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)  # 마지막으로 현재 연산자 삽입
        
        else: #피연산자이면
            output.append(term) #바로 출력
            
    while not s.isEmpty():   #처리가 끝났으면 스택에 남은 항목을
        output.append(s.pop())   # 모두 출력
        
    return output    #결과(후위 표기식 리스트)를 반환

# 위에서 만든 함수 실행 프로그램
infix1 = ['8','/','2','-','3','+','(','3','*','2',')'] #8/2-3+(3*2)
infix2 = ['1','/','2','*','4','*','(','1','/','4',')'] #1/2*4*(1/4)
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print(' 중위표기: ',infix1)
print(' 후위표기: ',postfix1)
print(' 계산결과: ',result1, end='\n\n')
print(' 중위표기: ',infix2)
print(' 후위표기: ',postfix2)
print(' 계산결과: ',result2)
