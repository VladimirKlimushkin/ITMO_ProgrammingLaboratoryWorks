a = 1000
b = a
c = int("1000")

print("Типы:", type(a), type(b), type(c)) # int, int, int
print("Идентификаторы:", id(a), id(b), id(c)) # id каждого из объектов
print("a == b:", a == b) # a == b: True
print("a is b:", a is b) # a is b: True
print("a == c:", a == c) # a == c:
print("a is c:", a is c)
