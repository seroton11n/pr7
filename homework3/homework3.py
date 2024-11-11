number = int(input("Введите десятичное число: "))
base = int(input("Введите основание системы счисления (2, 8, 16): "))
if base == 2:
    result = bin(number)[2:]  # удаляем префикс '0b'
elif base == 8:
    result = oct(number)[2:]  # удаляем префикс '0o'
elif base == 16:
    result = hex(number)[2:]  # удаляем префикс '0x'
else:
    result = "Неподдерживаемая система счисления"
print(f"Число {number} в системе счисления с основанием {base} равно {result}")
