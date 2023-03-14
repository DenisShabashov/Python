tickets = int(input("При покупке от 4-х билетов действует скидка 10% от стоимости заказа!\n"
                           'Сколько билетов вы хотите приобрести?  '))
total = 0
for i in range(tickets):
    age = int(input('Введите возраст >>> '))
    if 18 <= age < 25:
        total += 990
    elif age >= 25:
        total += 1390
if total >= 3960:
    total -= (total//10)
print(total)