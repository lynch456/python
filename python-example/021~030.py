# 021 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예
# p t
Letters = 'python'
print(Letters[0], Letters[2])

# 022 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[4:])

# 023 래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
string = "홀짝홀짝홀짝"
print(string[::2])

# 024 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예:
# NOHTYP
string = "PYTHON"
print(string[::-1])

# 025 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222
phone_number = "010-1111-2222"
print(phone_number[0:3], phone_number[4:8], phone_number[9:])
phone_number1 = phone_number.replace("-", " ")  # .replace("") 문자열 제거하고 그대로 출력
print(phone_number1)

# 26번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')  # .replace('') 문자열 제거하고 붙임 출력
print(phone_number1)

# 027 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예:
# kr
url = "http://shareboo.kr"
print(url[-2:])
url_split = url.split('.')  # .split() 지정된 곳을 기준으로 분리
print(url_split[-1])

# 028 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
# lang = 'python'
# lang[0] = 'P'
# print(lang) 실행 안됨. 문자열은 수정 불가능

# 029 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
string = 'abcdfe2a354a32'
string1 = string.replace('a', 'A')
print(string1)

# 030 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
string = 'abcd'
string.replace('a', 'b')
print(string)  # 문자열은 변경할 수 없는 자료형이라 abcd그대로 출력됨
