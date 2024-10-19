num = int(input('Введите число от 3 до 20: '))
p = []
for i in range(1, 20):
    for j in range(1, 20):
        sum_ = i + j
        if i != j:
            if i >= j:
                continue
            if sum_ == num or num % sum_ == 0:
                result = str(i) + str(j)
                p.append(result)

print(f'Пароль для числа {num}: ', *p, sep = '')