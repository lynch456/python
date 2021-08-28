
# print("이름 : ", end="")
# print(name)
# print("나이 : ", end="")
# print(age, end="살\n")
# print("키 : ", end="")
# print(height, end="cm\n")
# print("취미 : ", end="")
# print(hobby)

# 서식문자(format)
# 반드시 따옴표 안에서 작성한다.
# %d정수  %f실수  %c문자  %s문자열
name = "kimiksoo"
age = 10
height = 120.123
hobby = "piano"

print("이름 : %s" % name)
print("나이 : %d" % age)
print("키 : %.3fcm" % height)
print("취미 : %s" % hobby)
