amount_due = 50
while amount_due > 0:
    print(f"Нужная сумма: {amount_due}")
    coin = int(input("Вставьте монету: "))
    if coin in [50, 5, 20, 10]:
        amount_due -= coin

change_owed = -amount_due
print(f"Ваша сдача: {change_owed}")