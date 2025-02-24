# Zusammenarbeit mit folgenden Teilnehmern:
def cross_sum(n, b):
    if b < 2:
        raise ValueError("b must be greater than 2")
    if n < 0:
        raise ValueError("n must be a natural number")
    sum = 0
    while n >= 1:
        rest = n % b
        n //= b
        sum += rest
    return sum
