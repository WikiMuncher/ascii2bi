# This is a sample Python script.
print("<선택>")
print("1. 입력한 ascii를 바이너리로 변환")
print("2. 입력한 바이너리를 ascii로 변환")

select = input()

def bi2ascii(orgWords):
    resultword = ""
    for a in orgWords.split():
        resultword += chr(int(a, 2))
    print(resultword)


def ascii2bi(orgWords):
    for a in orgWords:
        print(str.lstrip(bin(ord(a)), "0b"), end=" ")


if select == "1":
    print("ascii to bi")
    ascii2bi(input())
elif select == "2":
    print("bi to ascii")
    bi2ascii(input())
else:
    print("unidentified select")

print("\n---------------------")
input("press any key to exit")