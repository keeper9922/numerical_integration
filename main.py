from funcs import rect, trapezoidal, simpson
from funcs import f
def full_pass(func, a, b, divisions):
    for i in range(1, 2+1):
        print(f"\n{i}N = {i * divisions}:")
        print(rect(func, a, b, divisions))
        print(trapezoidal(func, a, b, divisions))
        print(simpson(func, a, b, divisions))

N = 10000
if __name__ == "__main__":
    full_pass(f, 0, 1, N)