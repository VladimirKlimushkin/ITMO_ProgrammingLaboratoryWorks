## Задание 1

### Выражения
- `"Python"` - строковый литерал
- `4`, `2` - целочисленные литералы
- `4 * 2` - арифметическое выражение
- `course`, `hours` - обращения к именам
- `f"{course}: {hours} часов"` - f-строка
- `print(...)` - вызов функции (значение — None)

### Инструкции
- `course = "Python"` - присваивание
- `hours = 4 * 2` - присваивание
- `print(f"...")` - expression statement (инструкция-выражение)

### Литералы
- `"Python"` (str)
- `4`, `2` (int)
- `f"{course}: {hours} часов"` (f-string)

### Имена, создаваемые программой
- `course` -> "Python"
- `hours` -> 8
- `print` -> не создаётся программой, а берётся из builtins



## Задание 2

### Прогнозы результатов
print("a == b:", a == b) # a == b: True
print("a is b:", a is b) # a is b: True
print("a == c:", a == c) # a == c: True
print("a is c:", a is c) # a is c: False

graph LR
    A["имя a"] --> OBJ1["объект int: 1000<br/>id = X"]
    B["имя b"] --> OBJ1
    C["имя c"] --> OBJ2["объект int: 1000<br/>id = Y"]

    style OBJ1 fill:#cde
    style OBJ2 fill:#dec
    
_________________++_______
