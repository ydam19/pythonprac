
# Day 5: 정규표현식 심화, 예외처리
import re

# 1. 패턴 찾기 (search, match)
print("[1] search, match")
text = "Apple 100, Banana 200, Orange 300"
print(re.search(r"[0-9]+", text).group())
print(re.match(r"[A-Za-z]+", text).group())
print(re.match(r"[0-9]+", text))
# 한 줄 설명: search는 글 전체에서 처음 맞는 부분을, match는 글의 맨 앞이 맞는지만 확인해서, 찾으면 group()으로 꺼내고 못 찾으면 None을 돌려준다.
# 출력 결과:
# 100
# Apple
# None

# 2. 글 나누기 (split)
print("\n[2] split")
text = "Apple 100, Banana 200, Orange 300"
print(re.split(r",\s*", text))
# 한 줄 설명: 쉼표와 그 뒤의 공백을 기준으로 글을 잘라서 리스트로 만든다.
# 출력 결과:
# ['Apple 100', 'Banana 200', 'Orange 300']

# 3. 형식 검사 (fullmatch)
print("\n[3] fullmatch")
phone_pattern = r"010-[0-9]{4}-[0-9]{4}"
print(bool(re.fullmatch(phone_pattern, "010-1234-5678")))
print(bool(re.fullmatch(phone_pattern, "010-12-5678")))
print(bool(re.fullmatch(r"[A-Za-z0-9._]+@[A-Za-z0-9.]+\.[a-z]+", "test@example.com")))
# 한 줄 설명: 글 전체가 패턴과 딱 맞는지 검사해서 전화번호와 이메일 형식이 맞으면 True, 틀리면 False를 출력한다.
# 출력 결과:
# True
# False
# True

# 4. 예외처리 (try, except)
print("\n[4] try, except")
for value in ["10", "abc", "30"]:
    try:
        print(int(value) * 2)
    except ValueError:
        print(value, "는 숫자가 아니다")
# 한 줄 설명: 문자열을 숫자로 바꿔 2배로 출력하다가 숫자가 아닌 값에서 에러가 나도 except로 받아서 프로그램이 멈추지 않고 다음 값으로 넘어간다.
# 출력 결과:
# 20
# abc 는 숫자가 아니다
# 60