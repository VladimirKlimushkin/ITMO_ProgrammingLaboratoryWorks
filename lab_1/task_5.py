researcher = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs = int(input("Количество запусков: "))
duration = float(input("Длительность одного запуска (с): "))
real = float(input("Действительная часть коэффициента: "))
imag = float(input("Мнимая часть коэффициента: "))

total_seconds = runs * duration
total_minutes = total_seconds / 60
coefficient = complex(real, imag)
mod_squared = real ** 2 + imag ** 2
has_runs = bool(runs)

print("=" * 40)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {mod_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)

print("Типы введённых значений:")
print(f"  researcher: {type(researcher).__name__}")
print(f"  experiment: {type(experiment).__name__}")
print(f"  runs:       {type(runs).__name__}")
print(f"  duration:   {type(duration).__name__}")
print(f"  real:       {type(real).__name__}")
print(f"  imag:       {type(imag).__name__}")
