def add (x,y):
    return x + y
def sub (x,y):
    return x - y
def mul (x,y):
    return x * y
def div (x,y):
    if y == 0:
        return 'Деление на ноль невозможно!'
    return x / y

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")
if choice not in ('1', '2', '3', '4'):
    print('Операция выбрана некорректно')
else:
    print('Операция выбрана корректно')

if choice == '1' or choice == '2' or choice == '3' or choice == '4':
    print('Вы можете ввести целое число или же дробное, но через точку')
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        print('Ваш результат:', add(num1,num2))
    elif choice == '2':
        print('Ваш результат:', sub(num1,num2))
    elif choice == '3':
        print('Ваш результат:', mul(num1, num2))
    elif choice == '4':
        print('Ваш результат:', div(num1,num2))
