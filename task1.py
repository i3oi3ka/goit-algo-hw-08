import heapq
from typing import List


def minimize_connection_cost(cable_lengths: List[int]) -> int:
    # Ініціалізуємо мін-купу з початковими довжинами кабелів
    heapq.heapify(cable_lengths)

    total_cost = 0  # Змінна для збереження загальних витрат на з'єднання

    # Об'єднуємо кабелі, поки не залишиться один
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротші кабелі для з'єднання
        shortest_cable = heapq.heappop(cable_lengths)
        second_shortest_cable = heapq.heappop(cable_lengths)

        connection_cost = shortest_cable + second_shortest_cable
        total_cost += connection_cost  # Додаємо витрати на поточне з'єднання

        # Додаємо новий кабель назад у купу
        heapq.heappush(cable_lengths, connection_cost)

    return total_cost


# Тестовий приклад
cable_lengths = [1, 2, 10, 45, 12, 3, 14]
print("Загальні витрати:", minimize_connection_cost(cable_lengths))
