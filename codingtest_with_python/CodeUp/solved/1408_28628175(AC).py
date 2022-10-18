"""
인터넷 서비스들은 대부분 아이디와 패스워드(password)를 이용한다.

이때 사용되는 패스워드는 여러 가지 방법으로 암호화되어 저장된다.

[어떤 인터넷 서비스의 2가지 암호화 방법]

- 입력받은 문자의 ASCII 코드값 + 2

- (입력받은 문자의 ASCII 코드값 * 7) % 80 + 48

사용자의 패스워드를 2가지 방법으로 암호화한 결과를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 20자 이내로 구성된 암호를 입력한다.(단, 입력되는 암호에 공백은 포함되어있지 않다.)

출력
① 첫 번째 줄에는 첫 번째 방식으로 암호화한 결과를 출력 한다.

② 두 번째 줄에는 두 번째 방식으로 암호화한 결과를 출력 한다.

입력 예시   
TEST

출력 예시
VGUV
L3EL
"""

password = input()
encoded_password1 = ''  # 첫 번째 방식으로 암호화된 결과 저장할 변수 선언
encoded_password2 = ''  # 두 번째 방식으로 암호화된 결과 저장할 변수 선언

for c in password: # 입력받은 암호에서 한 문자씩 가져와서
    encoded_password1 = encoded_password1 + chr(ord(c) + 2) # 첫 번째 방식으로 암호화
    encoded_password2 = encoded_password2 + chr(((ord(c) * 7) % 80) + 48) # 두 번째 방식으로 암호화

print(encoded_password1) # 첫 번째 방식으로 암호화된 결과 출력
print(encoded_password2) # 두 번째 방식으로 암호화된 결과 출력
