def check_prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            return False
        return True
number = int(input('판별한 자연수를 입력하세요:'))
print(check_prime_num(number))
