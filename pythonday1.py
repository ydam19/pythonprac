def triangle(lines):
    """1, 2, 3, ... 개씩 늘어나는 삼각형 (C: j <= i)"""
    for i in range(lines):
        for j in range(i + 1):
            print("*", end="")
        print()


def odd_triangle(lines):
    """1, 3, 5, ... 개씩 늘어나는 삼각형 (C: j <= 2*i)"""
    for i in range(lines):
        for j in range(2 * i + 1):
            print("*", end="")
        print()


def even_triangle(lines):
    """2, 4, 6, ... 개씩 늘어나는 삼각형 (C: j <= 2*i + 1)"""
    for i in range(lines):
        for j in range(2 * i + 2):
            print("*", end="")
        print()


def reverse_triangle(lines):
    """lines, lines-1, ..., 1 개씩 줄어드는 삼각형 (C: j를 10에서 i까지 감소)"""
    for i in range(lines, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


def hourglass():
    """가운데가 빈 모래시계 모양 (C: 별 i개 + 공백 (5-i)*2개 + 별 i개)"""
    for i in range(5, 0, -1):          # 위쪽: 5 -> 1
        print("*" * i + " " * ((5 - i) * 2) + "*" * i)
    for i in range(2, 6):              # 아래쪽: 2 -> 5
        print("*" * i + " " * ((5 - i) * 2) + "*" * i)


def repeat_triangle(count):
    """삼각형을 count번 반복 (C: printStar(int count))"""
    for n in range(count):
        triangle(10)


def main():
    print("[1] 삼각형")
    triangle(10)

    print("\n[2] 홀수 삼각형 (1, 3, 5, ...)")
    odd_triangle(10)

    print("\n[3] 짝수 삼각형 (2, 4, 6, ...)")
    even_triangle(5)

    print("\n[4] 거꾸로 삼각형")
    reverse_triangle(10)

    print("\n[5] 모래시계")
    hourglass()

    print("\n[6] 삼각형 3번 반복")
    repeat_triangle(3)


if __name__ == "__main__":
    main()
