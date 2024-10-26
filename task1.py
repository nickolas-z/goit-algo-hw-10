import heapq

def display_heap(cables)->None:
    """ Вивести поточний стан купи """
    print(f"Поточна купа: {cables}")

def minimize_cable_cost(cables)->tuple:
    """ Знайти мінімальні витрати на з'єднання кабелів """
    # Перевірка, чи потрібно взагалі з'єднувати кабелі
    if len(cables) < 2:
        return 0, []
    
    # Зберігаємо початкову загальну довжину
    total_length = sum(cables)

    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    display_heap(cables)
    
    total_cost = 0
    connections = []

    # Поки у нас є більше ніж один кабель у купі
    while len(cables) > 1:
        # Витягуємо два найкоротших кабеля
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # З'єднуємо їх
        cost = first + second
        total_cost += cost
        
        # Додаємо з'єднаний кабель назад до купи
        heapq.heappush(cables, cost)

        # Зберігаємо з'єднання для виведення
        connections.append((first, second))
        display_heap(cables)
    
    return total_cost, connections, total_length

def main():
    cable_lengths = [4, 3, 2, 6]

    total_cost, connections, total_length = minimize_cable_cost(cable_lengths)
    print("\nПорядок з'єднання кабелів:")
    for i, (first, second) in enumerate(connections, 1):
        print(f"{i}. З'єднати кабелі довжиною {first} та {second}")
    print(f"\nЗагальна довжина кабеля: {total_length}")
    print(f"Мінімальні загальні витрати на з'єднання: {total_cost}")

if __name__ == "__main__":
    main()