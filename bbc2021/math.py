from typing import *

def is_multiple(n: int, f: int) -> bool:
    return not bool(n % f)


def multiples35(limit: int) -> int:
    def _is_multiple_35(n: int) -> bool:
        return is_multiple(n, 3) or is_multiple(n, 5)
    return sum(filter(_is_multiple_35, range(1, limit)))


def fibonacci_l(limit: int) -> Generator[int, int, None]:
    a, b = 0, 1
    while b < limit:
        a, b = b, a
        b += a
        if b < limit:
            yield b


def even_fibonacci(limit: int) -> int:
    return sum(filter(lambda f: f % 2 == 0, fibonacci_l(limit)))


def lpfactor(number: int) -> int:
    i: int = 2
    while i*i < number:
        while number % i == 0:
            number //= i
        i += 1
    
    if number < i:
        return i-1
    else:
        return number


def lpalindrome() -> int:
    greatest: int = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            num: int = i*j
            rep = str(num)
            if rep == rep[::-1] and num > greatest:
                greatest = num
    return greatest
