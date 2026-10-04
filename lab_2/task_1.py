a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10, 20, 30]  # переназначение на новый список
print(first == second) # значения равны
print(first is second) # разные объекты

second.append(40) # меняем новый список
print(first)      # first не изменился
print(second)     # [10, 20, 30, 40]