import math


# A
x = 17
y = 5
print("A:", x + y, type(x + y))
print("A:", x - y, type(x - y))
print("A:", x * y, type(x * y))
print("A:", x / y, type(x / y))
print("A:", x // y, type(x // y))
print("A:", x % y, type(x % y))
print("A:", x ** y, type(x ** y))

# B
big = 2 ** 1000
print("B:", big)
print("B: length in bits ", big.bit_length())

# C
result = 0.1 + 0.2
print("C: result =", result)
print("C: result == 0.3:", result == 0.3)
print("C: result - 0.3 =", result - 0.3)
print("C: math.isclose:", math.isclose(result, 0.3))

# D
print("D:", int("42"), type(int("42")))
print("D:", float("3.14"), type(float("3.14")))
print("D:", str(2026), type(str(2026)))
print("D:", bool(0), type(bool(0)))
print("D:", bool(-1), type(bool(-1)))
print("D:", bool(""), type(bool("")))
print("D:", bool("False"), type(bool("False")))
z = complex(2, -3)
print("D:", z, type(z))
print("D: real =", z.real, "imag =", z.imag)
