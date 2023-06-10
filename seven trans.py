def f1(x: int):
    b = int(x)
    x1 = 0b1111 & b
    x2 = 0b11111111 & (b >> 4)
    x3 = 0b1111 & (b >> 12)
    return {
        "X1": x1,
        "X2": x2,
        "X3": x3
    }


def f2(dct):
    x1 = int(dct["X1"]) << 8
    x2 = int(dct["X2"])
    x3 = int(dct["X3"]) << 18
    return x1 | x2 | x3


def main1(num: str):
    num1 = int(num, 16)
    dct = f1(int(num1))
    return str(f2(dct))


print(main1('0xc8e4'))

# Транскодирование, вход 16ая строка, выход 10
