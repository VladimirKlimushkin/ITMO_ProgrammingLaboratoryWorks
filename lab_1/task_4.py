student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print("Первый:", student[0])
print("Последний:", student[-1])

name = student[:4]
surname = student[5:]
print("Имя:", name)
print("Фамилия:", surname)

print("Верхний:", student.upper())
print("Нижний:", student.lower())

initials = student[0] + "." + student[5] + "."
print("Инициалы:", initials)

print("Реверс:", course[::-1])

percent = completed / total * 100

line1 = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
line2 = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
line3 = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"
print(line1)
print(line2)
print(line3)

symbol = "Я"
print("Символ:", symbol)
print("Кодовая позиция:", ord(symbol))
print("Восстановленный:", chr(ord(symbol)))
encoded = symbol.encode("utf-8")
print("UTF-8 байты:", encoded)
print("Длина байтов:", len(encoded))
