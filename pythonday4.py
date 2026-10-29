import re
text = "Apple 100, Banana 200, Orange 300"

# 숫자만 추출
print(re.findall(r"[0-9]+", text))

# 영어 단어만 추출
print(re.findall(r"[A-Za-z]+", text))

# 숫자를 *로 변경
print(re.sub(r"[0-9]+", "*", text))