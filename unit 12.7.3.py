per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input("Введите сумму ")
vklad_tkb = int(money)/100*5.6
vklad_skb = int(money)/100*5.9
vklad_vtb = int(money)/100*4.28
vklad_sber = int(money)/100*4.0
deposit = [int(vklad_tkb), int(vklad_skb), int(vklad_vtb), int(vklad_sber)]
print(deposit)

max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать", max_deposit)

