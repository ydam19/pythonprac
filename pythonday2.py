# ───────── 별 다섯줄만 출력 (1) - break ─────────
print("[1] break")
for i in range(10):
    if i == 5:
        break

    for j in range(i + 1):
        print("*", end="")
    print()


# ───────── 별 다섯줄만 출력 (2) - continue ─────────
print("\n[2] continue")
for i in range(10):
    if i >= 5:
        continue

    for j in range(i + 1):
        print("*", end="")
    print()


# ───────── 배열: 다섯 개의 합 구하기 ─────────
print("\n[3] 다섯 개의 합")
person = [10, 20, 30, 40, 50]

for i in range(1, 5):
    person[0] += person[i]

print("total:", person[0])


# ───────── 배열: 백 개의 합 구하기 ─────────
print("\n[4] 백 개의 합")
person = [0] * 100
total = 0

for i in range(100):
    person[i] = i + 1

for i in range(100):
    total += person[i]

print("합계:", total)