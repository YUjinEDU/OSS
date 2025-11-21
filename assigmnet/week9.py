


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")


x = 3
y = 2
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")


money = 2000
card = True
print(f"돈이 3000원 이상 있거나 카드가 있다면: {money >= 3000 or card}")
print(f"돈이 3000원 이상 있고 카드가 있다면: {money >= 3000 and card}")


pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


score = 85
message = "success" if score >= 60 else "failure"
print(f"점수: {score}, 결과: {message}")



# 문제 1-1: 나이별 요금 계산
print("\n문제 1-1: 나이별 요금 계산")
ages_to_test = [5, 12, 18, 25]  # 테스트할 나이들
for age in ages_to_test:
    if age < 8:
        fee = 0
    elif age < 14:
        fee = 500
    elif age < 20:
        fee = 1000
    else:
        fee = 1500
    print(f"나이 {age}세의 요금은 {fee}원입니다.")

# 문제 1-2: 로그인 시스템
print("\n문제 1-2: 로그인 시스템")
test_cases = [("admin", "1234"), ("admin", "wrong"), ("user", "1234")]
for user_id, user_password in test_cases:
    if user_id == "admin" and user_password == "1234":
        print(f"아이디: {user_id}, 비밀번호: {user_password} -> 로그인 성공!")
    else:
        print(f"아이디: {user_id}, 비밀번호: {user_password} -> 로그인 실패!")

# ============================================
# 03-2 while 문 실습
# ============================================



treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무 넘어갑니다!")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print(f"남은 커피의 양은 {coffee}개입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

# ============================================
# 실습 문제 2: while 문 연습
# ============================================

sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(f"1부터 10까지의 합: {sum}")

# 문제 2-2: 비밀번호 맞추기 게임
print("\n문제 2-2: 비밀번호 맞추기 게임")
password = "python"
max_attempts = 3

# 시뮬레이션: 여러 시도 케이스 테스트
test_inputs = ["wrong1", "python", "wrong2"]  # 마지막은 시도하지 않음
attempts = 0
success = False

for user_input in test_inputs:
    attempts += 1
    print(f"시도 {attempts}: 비밀번호 입력 - {user_input}")
    if user_input == password:
        print("비밀번호가 맞습니다!")
        success = True
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"틀렸습니다. {remaining}번 남았습니다.")
        else:
            print("비밀번호 입력 횟수를 초과했습니다.")
            break

if not success and attempts < max_attempts:
    print("게임 종료")

# ============================================
# 03-3 for 문 실습
# ============================================



test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 2. 다양한 for 문 사용
print("\n2. 다양한 for 문 사용")
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# 3. for 문의 응용
print("\n3. for 문의 응용")
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")

# 4. for 문과 continue
print("\n4. for 문과 continue")
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")

# 5. range() 함수
print("\n5. range() 함수")
print("range(10):", list(range(10)))
print("range(1, 11):", list(range(1, 11)))
print("range(1, 10, 2):", list(range(1, 10, 2)))

# 6. for 문과 range() 함수
print("\n6. for 문과 range() 함수")
for i in range(1, 11):
    print(i, end=' ')
print()

# ============================================
# 실습 문제 3: for 문 연습
# ============================================
print("\n" + "="*30 + " 실습 문제 3: for 문 " + "="*30)

# 문제 3-1: 구구단 출력
print("\n문제 3-1: 구구단 출력")
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end='\t')
    print()

# 문제 3-2: 리스트 컴프리헨션
print("\n문제 3-2: 리스트 컴프리헨션")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"원본 리스트: {numbers}")
print(f"제곱 리스트: {squares}")

# ============================================
# 통합 실습 문제
# ============================================
print("\n" + "="*30 + " 통합 실습 문제 " + "="*30)

# 문제 4: 간단한 계산기 프로그램
print("\n문제 4: 간단한 계산기 프로그램")
print("계산기 테스트 케이스들:")

# 테스트 케이스들
test_operations = [
    (1, 10, 5),  # 덧셈: 10 + 5
    (2, 10, 5),  # 뺄셈: 10 - 5
    (3, 10, 5),  # 곱셈: 10 * 5
    (4, 10, 5),  # 나눗셈: 10 / 5
    (4, 10, 0),  # 나눗셈: 0으로 나누기 테스트
]

for choice, num1, num2 in test_operations:
    print(f"\n선택: {choice}, 숫자: {num1}, {num2}")

    if choice == 1:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("0으로 나눌 수 없습니다.")

print("\n계산기 테스트가 완료되었습니다.")

print("\n" + "="*50)
print("점프투파이썬 Chapter 7 실습이 완료되었습니다!")
print("="*50)
