number = int(input("Введите десятичное число: "))
if number == 0:
    result = "0"
else:
    result = ""
    while number > 0:
        result = str(number % 5) + result
        number //= 5
print(f"Число в пятеричной системе счисления: {result}")
