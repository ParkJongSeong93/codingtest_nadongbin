import sys

def main():
    N = int(sys.stdin.readline())

    students = []
    for _ in range(N):
        student, korean, english, math = map(str, sys.stdin.readline().split())
        students.append((student, int(korean), int(english), int(math)))

    students.sort(key= lambda item : (-item[1], item[2], -item[3], item[0]))

    for student, _, _, _ in students:
        print(student)

main()

# 만약 이름이 내림차순이라면
# students.sort(key= lambda item : item[0], reverse= True)
# students.sort(key= lambda item: (-item[1], item[2], -item[3]))