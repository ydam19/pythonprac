# Day 3: 문자열, 리스트, 튜플, 딕셔너리, 함수, 클래스

# 1. 문자열의 글자를 하나씩 출력
print("[1] 문자열 글자 하나씩")
array = "Hello"
for i in range(5):
    print(i, "번째 문자의 값", array[i])
# 한 줄 설명: i를 0~4로 돌리며 문자열 "Hello"의 i번째 글자를 번호와 함께 출력한다.

# 2. 문자열 출력
print("\n[2] 문자열 출력")
pstr = "아름다운 지구입니다."
string = "how do you do!"
print("문자열 출력1", pstr)
print("문자열 출력2", string)
# 한 줄 설명: 문자열 두 개를 변수에 담아 각각 제목과 함께 출력한다.

# 3. 글자를 리스트에 담기
print("\n[3] 글자 리스트")
letters = ['H', 'e', 'l', 'l', 'o']
for i in range(5):
    print(i, "번째 문자의 값", letters[i])
# 한 줄 설명: 글자 5개를 리스트에 담고 i번째 글자를 번호와 함께 출력한다.

# 4. 글자 수 세기
print("\n[4] len()")
string = "how do you do!"
print("Hello 의 글자 수:", len("Hello"))
for i in range(len(string)):
    print(string[i], end="")
print()
# 한 줄 설명: len()으로 글자 수를 구해 출력하고, 그 수만큼 반복해 문자열을 글자 하나씩 이어서 출력한다.

# 5. 거꾸로 출력
print("\n[5] 거꾸로 출력")
array = "Hello"
for i in range(4, -1, -1):
    print(array[i], end="")
print()
# 한 줄 설명: i를 4에서 0까지 줄여가며 "Hello"를 뒤에서부터 출력해 "olleH"를 만든다.

# 6. 리스트 값 바꾸기
print("\n[6] 리스트 값 바꾸기")
letters = ['H', 'e', 'l', 'l', 'o']
letters[0] = 'J'
for i in range(5):
    print(letters[i], end="")
print()
# 한 줄 설명: 리스트의 0번째 글자를 'J'로 바꾸고 전체를 이어서 출력해 "Jello"를 만든다.

# 7. 매개변수와 return이 있는 함수
def myhap(max):
    hap = 0
    for i in range(1, max + 1):
        hap += i
    return hap


print("\n[7] 함수로 합계 구하기")
hap = myhap(10)
print("합계:", hap)
print("1부터 100까지의 합:", myhap(100))
# 한 줄 설명: 1부터 max까지의 합을 return으로 돌려주는 myhap 함수를 만들고, myhap(10)=55와 myhap(100)=5050을 출력한다.

# 8. 리스트와 튜플 (1차원)
print("\n[8] 리스트와 튜플")
array = [1, 2, 3, 4, 5]

print( array )

for value in array:
    print(value)

print(type(array))
array = (1, 2, 3, 4, 5)

print(array)
for value in array:
    print(value)

print(type(array))
# 한 줄 설명: 리스트와 튜플을 각각 통째로 출력하고, for로 값을 하나씩 꺼내 출력하고, type()으로 종류(list, tuple)를 확인한다.

# 9. 2차원 리스트와 2차원 튜플
print("\n[9] 2차원 리스트와 튜플")
array2 = [[1, 2, 3], [4, 5, 6]]
print(array2)
print(array2[0])

print(array2[1])
print(array2[0][0])
print(array2[0][1])
print(array2[0][2])
print(array2[1][0])
print(array2[1][1])
print(array2[1][2])

array2 = ((1, 2, 3), (4, 5, 6))
print(array2)
print(array2[0])
print(array2[1])
print(array2[0][0])
print(array2[0][1])
print(array2[0][2])
print(array2[1][0])
print(array2[1][1])
print(array2[1][2])
# 한 줄 설명: 2차원 리스트와 2차원 튜플을 각각 출력하고, array2[행][열]처럼 인덱스를 두 번 써서 값 6개를 하나씩 꺼낸다.

# 10. 딕셔너리
print("\n[10] 딕셔너리")
animal = {"TIGER" : "호랑이", "DOG" : "강아지","CAT" : "고양이"}

print(animal)

print(animal["TIGER"])
print(animal["DOG"])
print(animal["CAT"])

item = 'CAT'

if item in animal:
    print('CAT이 animal에 있습니다')

    item = 'FISH'
if item not in animal:
    print('FISH가 animal에 없습니다')
# 한 줄 설명: 키와 값을 짝지은 딕셔너리를 만들어 키로 값을 꺼내고, in / not in으로 키가 있는지 없는지 검사해 결과를 출력한다.

# 11. 클래스
print("\n[11] 클래스")
class Star :
    def __init__(self,line):

        self.line = line

    def set(self, line):
        self.line = line
    def get(self):
        return self.line

    def printStar(self):
        for i in range(1, self.line + 1):
            for j in range(1, i + 1):
                print("*", end="")
            print('\n', end="")


star = Star(5)
star.set(5)
star.printStar()
# 한 줄 설명: 줄 수를 저장하는 Star 클래스를 만들고, line이 5인 객체로 printStar를 호출해 1~5개짜리 별 삼각형을 출력한다.