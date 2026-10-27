
# 1. 기본 삼각형: i는 0~9, j는 0~i
print("[1] 삼각형") 
for i in range(10):
    for j in range(i + 1):
        print("*", end="")
    print()

# 2. 홀수 삼각형: j <= 2*i
print("\n[2] 1, 3, 5, ... 개")
for i in range(10):
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# 3. 거꾸로 삼각형: i는 0~10, j는 10에서 i까지 감소
print("\n[3] 11, 10, ... 1개")
for i in range(11):
    for j in range(10, i - 1, -1):
        print("*", end="")
    print()

# 3. 거꾸로 삼각형: i는 0~10, j는 10에서 i까지 감소
print("\n[3] 11, 10, ... 1개")
for i in range(11):
    for j in range(10, i - 1, -1):
        print("*", end="")
    print()

# 4. i를 2씩 증가: i는 0, 2, 4, 6, 8
print("\n[4] 1, 3, 5, 7, 9개")
for i in range(0, 10, 2):
    for j in range(i + 1):
        print("*", end="")
    print()

# 5. i를 2부터 10까지 2씩 증가, j < i
print("\n[5] 2, 4, 6, 8, 10개")
for i in range(2, 11, 2):
    for j in range(i):
        print("*", end="")
    print()

# 6. 모래시계: 별 i개 + 공백 (5-i)*2개 + 별 i개
print("\n[6] 모래시계")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range((5 - i) * 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
for i in range(2, 6):
    for j in range(i):
        print("*", end="")
    for j in range((5 - i) * 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 7. 삼각형을 3번 반복: 바깥에 n 반복 추가
print("\n[7] 삼각형 3번")
for n in range(3):
    for i in range(10):
        for j in range(i + 1):
            print("*", end="")
        print()


# 8. 함수로 묶기: printStar() 5번 호출
def printStar():
    for i in range(10):
        for j in range(i + 1):
            print("*", end="")
        print()


print("\n[8] printStar() 5번 호출")
printStar()
printStar()
printStar()
printStar()
printStar()

# 9. for문으로 printStar() 5번 호출
print("\n[9] for문으로 5번 호출")
for n in range(5):
    printStar()
