from pulp import *

def main():
    # Створюємо модель
    model = LpProblem("Оптимізація_виробництва_напоїв", LpMaximize)

    # Визначаємо кількість лимонаду та фруктового соку
    lemonade = LpVariable("Лимонад", 0, None, LpInteger)
    fruit_juice = LpVariable("Фруктовий_сік", 0, None, LpInteger)  

    # Цільова функція - максимізація загальної кількості продуктів
    model += lemonade + fruit_juice, "Загальна_кількість_продуктів"

    # Обмеження
    # Вода (2*лимонад + 1*фруктовий_сік <= 100)
    model += 2 * lemonade + fruit_juice <= 100, "Обмеження_води"
    # Цукор (1*лимонад <= 50)
    model += lemonade <= 50, "Обмеження_цукру"
    # Лимонний сік (1*лимонад <= 30)
    model += lemonade <= 30, "Обмеження_лимонного_соку"
    # Фруктове пюре (2*фруктовий_сік <= 40)
    model += 2 * fruit_juice <= 40, "Обмеження_фруктового_пюре"

    model.solve()

    print("Статус розв'язку:", LpStatus[model.status])
    print(f"\nОптимальні значення виробництва:")
    print(f"\tЛимонад: {int(value(lemonade))} одиниць")
    print(f"\tФруктовий сік: {int(value(fruit_juice))} одиниць")
    print(f"\nЗагальна кількість продуктів: {int(value(lemonade + fruit_juice))} одиниць")

    print("\nВикористання ресурсів:")
    print(f"\tВода: {2*value(lemonade) + value(fruit_juice)}/100 одиниць")
    print(f"\tЛимонний сік: {value(lemonade)}/30 одиниць")
    print(f"\tФруктове пюре: {2*value(fruit_juice)}/40 одиниць")

if __name__ == "__main__":
    main()
