def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'

    base36 = ''
    while number != 0:
        number, i = divmod(number, 36)
        base36 = '0123456789abcdefghijklmnopqrstuvwxyz'[i] + base36

    return base36

def convert_base(a, n, b):
    decimal = int(n, a)
    if b == 8:
        answer = oct(decimal)[2:]
    elif b == 2:
        answer = bin(decimal)[2:]
    elif b == 16:
        answer = hex(decimal)[2:]
    elif b == 36:
        answer = base36_encode(decimal)
    else:
        answer = str(decimal)

    return answer

a, n, b = map(str, input().split())

a=int(a)
b=int(b)

print(convert_base(a, n, b))  # 결과: b