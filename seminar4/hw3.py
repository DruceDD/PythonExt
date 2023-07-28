# Возьмите задачу о банкомате из семинара 2:
# 1. Начальная сумма равна нулю.
# 2. Допустимые действия: пополнить, снять, выйти.
# 3. Сумма пополнения и снятия кратны 50 у.е.
# 4. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# 5. После каждой третей операции пополнения или снятия начисляются проценты - 3%
# 6. Нельзя снять больше, чем на счёте.
# 7. При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной.
# 8. Любое действие выводит сумму денег
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def atm():
    amount = 0
    count = 0
    commission = 30
    operations = []

    while True:
        action = input("Выберите действие: "
                       "\n1 - пополнить"
                       "\n2 - снять"
                       "\n3 - выйти"
                       "\nномер действия: ")

        if action == "1":
            amount, operation = deposit_money(amount, count, commission)
            operations.append(operation)
            count += 1
            if count % 3 == 0:
                amount = add_bonus(amount)

        elif action == "2":
            amount, operation = withdraw_money(amount, count, commission)
            operations.append(operation)
            count += 1
            if count % 3 == 0:
                amount = add_bonus(amount)

        elif action == "3":
            break

        else:
            print("Неверное действие")
        print(f"Сумма денег на счете: {amount} у.е.")

    print("Операции:")
    for operation in operations:
        print(operation)


def deposit_money(amount, count, commission):
    deposit = int(input("Введите сумму для пополнения (кратную 50): "))

    if deposit % 50 != 0:
        print("Сумма пополнения должна быть кратной 50")
        return amount, None

    if amount >= 5000000:
        amount -= amount * 0.1

    amount += deposit

    operation = f"Пополнение: +{deposit} у.е."

    return amount, operation


def withdraw_money(amount, count, commission):
    withdrawal = int(input("Введите сумму для снятия (кратную 50): "))

    if withdrawal % 50 != 0:
        print("Сумма снятия должна быть кратной 50")
        return amount, None

    if withdrawal > amount:
        print("Недостаточно средств на счете")
        return amount, None

    if amount >= 5000000:
        amount -= amount * 0.1

    if withdrawal * 0.015 > commission:
        commission = withdrawal * 0.015

    if withdrawal * 0.015 > 600:
        commission = 600

    if withdrawal < amount - commission:
        amount -= withdrawal + commission
        operation = f"Снятие: -{withdrawal} у.е., комиссия: {commission} у.е."
        return amount, operation

    else:
        print("Недостаточно средств на счете")
        return amount, None


def add_bonus(amount):
    amount += amount * 0.03
    return amount


atm()