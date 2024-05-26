a = int(input("수를 입력해 주세요: "))

if 1 <= a <= 9:
    for b in range(1, 10):
        print(f"{a} X {b} = {a*b}")
else:
    print("1~9 사이의 수를 입력해 주세요.")
