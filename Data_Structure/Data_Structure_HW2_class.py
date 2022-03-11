#Data_Structure_HW2class
#바이오메디컬공학부 손무현

class BankAccount :       #은행계좌클래스
  def __init__(self,name,number,money = 0) :    # 객체생성
     self.__name = name      
     self.__number = number
     self.__money = money
  
  def deposit(self,money) :
    self.__money += money
    
  def withdraw(self,money) :
    if self.__money >= money:
      self.__money -= money
      return True
    else :
      return False 


  def __str__(self) :
    return f"name: {self.__name}, number: {self.__number}, money: {self.__money}"


  def getName(self):
      return self.__name
  def getNumber(self):
      return self.__number
  def getMoney(self):
      return self.__money
      
#자료구조 	2장 과제_2 클래스 문제
#한국외국어대학교 바이오메디컬공학부 201804594 손무현

class Employee :  # 직원 클래스
  def __init__(self,name,base,extra=0): #생성자
    self.__name = name  #멤버변수(이름)
    self.__base = base  #멤버변수(기본금)
    self.__extra = extra #멤버변수(초과근무액)
  
  def calc_salary(self):  #멤버함수(기본금+초과근무액 리턴)
    return self.__base + self.__extra
  
  def plus_extra(self,num): #멤버함수(num을 받아 초과근무액에 더함)
    self.__extra += num

  def __str__(self):  #멤버함수(멤버변수들과 월급을 문자열로 생성,리턴)
    return (f"이    름 : {self.__name}\n기 본 금 : {self.__base}\n초과금액 : {self.__extra}\n총 월 급 : {self.calc_salary()}\n{'='*20}")
    
#부모Class의 private 멤버변수는 자식Class의 멤버함수에서 부를 수 없기 때문에
#get함수를 써서 가져옴    
  def getName(self):
    return self.__name
  def getBase(self):
    return self.__base
  def getExtra(self):
    return self.__extra
class Manager(Employee) : #매니저 클래스
  def __init__(self,name,base,add,extra=0): #생성자
    super().__init__(name,base,extra)  #부모(Employee)클래스의 생성자 호출
    self.__add = add #추가 멤버변수선언(메니저수당)
  
  def cal_salary(self):  #멤버함수(기본금+초과근무액+수당 리턴)
    return super().getBase() + super().getExtra() + self.__add  

  def __str__(self): #멤버함수(멤버변수들과 월급을 문자열로 생성,리턴)
    return (f"이    름 : {super().getName()}\n기 본 금 : {super().getBase()}\n초과금액 : {super().getExtra()}\n추가수당 : {self.__add}\n총 월 급 : {self.cal_salary()}\n{'='*20}")
    
  emp1 = Employee("홍길동",200)  #직원 객체 생성(이름:홍길동,기본금:200)
emp2 = Employee("이영희",220)  #직원 객체 생성(이름:이영희,기본금:220)
mana1 = Manager("김철수",250,30) #매니저 객체 생성(이름:김철수,기본금:250,매니저수당:30)

#객체 모두 초기값 출력
print(emp1)
print(emp2)
print(mana1)

# 초과근무 더하기
emp1.plus_extra(50)
emp1.plus_extra(60)
emp2.plus_extra(60)
emp2.plus_extra(60)
emp2.plus_extra(60)
mana1.plus_extra(50)
mana1.plus_extra(50)

#초과근무 더한 후 객체 출력
print("홍길동 : 초과근무액 50, 60 추가")
print(emp1)
print("이영희 : 초과근무액 60, 60, 60 추가")
print(emp2)
print("김철수 : 초과근무액 50, 50 추가")
print(mana1)
