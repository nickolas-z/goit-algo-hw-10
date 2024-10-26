import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції
def f(x)->float:
    """
    Функція, яку потрібно інтегрувати
    Args:
        x (float): значення аргументу
    Returns:
        float: значення функції в точці x
    """
    return x**2

def monte_carlo_integration(f, a, b, n)->float:
    """Метод Монте-Карло для обчислення інтегралу
    Args:
        f (function): функція, яку потрібно інтегрувати
        a, b (float): межі інтегрування
        n (int): кількість точок
    Returns:
        float: обчислена площа під кривою
    """
    # Генеруємо випадкові точки
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, f(b), n)

    # Підрахунок точок під кривою
    points_under = sum(y <= f(x))

    # Обчислення площі
    area = (b - a) * f(b) * (points_under / n)
    return area

def main():
    """Головна функція"""
    
    # Параметри інтегрування
    # межі
    a, b = 0, 2
    # кількість точок для методу Монте-Карло
    n_points = 100000

    # Виконання обчислень
    monte_carlo_result = monte_carlo_integration(f, a, b, n_points)
    analytical_result, error = quad(f, a, b)

    plt.figure("Візуалізація процесу", figsize=(12, 6))

    # Графік 1: Функція та точки Монте-Карло
    plt.subplot(1, 2, 1)
    x_plot = np.linspace(a, b, n_points)
    y_plot = f(x_plot)

    # Генеруємо точки для візуалізації
    n_vis = n_points//100
    x_points = np.random.uniform(a, b, n_vis)
    y_points = np.random.uniform(0, f(b), n_vis)
    under_curve = y_points <= f(x_points)

    plt.plot(x_plot, y_plot, "r-", label="f(x) = x²")
    plt.scatter(
        x_points[under_curve],
        y_points[under_curve],
        color="blue",
        alpha=0.1,
        label="Точки під кривою",
    )
    plt.scatter(
        x_points[~under_curve],
        y_points[~under_curve],
        color="red",
        alpha=0.1,
        label="Точки над кривою",
    )
    plt.fill_between(x_plot, y_plot, alpha=0.2)
    plt.grid(True)
    plt.legend()
    plt.title("Візуалізація методу Монте-Карло")

    # Графік 2: Збіжність методу
    plt.subplot(1, 2, 2)
    points_range = np.logspace(2, 5, 20, dtype=int)
    results = [monte_carlo_integration(f, a, b, n) for n in points_range]
    plt.semilogx(points_range, results, "b.-", label="Метод Монте-Карло")
    plt.axhline(
        y=analytical_result, color="r", linestyle="--", label="Аналітичний результат"
    )
    plt.grid(True)
    plt.legend()
    plt.title("Збіжність методу")
    plt.xlabel("Кількість точок")
    plt.ylabel("Значення інтеграла")

    plt.subplot(1, 2, 2)
    textstr = '\n'.join((
        f"Результат методу Монте-Карло (n = {n_points}): {monte_carlo_result:.6f}",
        f"Аналітичний результат: {analytical_result:.6f}",
        f"Абсолютна похибка: {abs(monte_carlo_result - analytical_result):.6f}",
        f"Відносна похибка: {abs(monte_carlo_result - analytical_result)/analytical_result*100:.4f}%"
    ))

    # Розміщення тексту на графіку
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.gca().text(0.15, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
                   verticalalignment='top', bbox=props)
    plt.tight_layout()
    plt.savefig("monte_carlo_integration.png")
    plt.show()

    print(f"Результат методу Монте-Карло (n = {n_points}): {monte_carlo_result:.6f}")
    print(f"Аналітичний результат: {analytical_result:.6f}")
    print(f"Абсолютна похибка: {abs(monte_carlo_result - analytical_result):.6f}")
    print(
        f"Відносна похибка: {abs(monte_carlo_result - analytical_result)/analytical_result*100:.4f}%"
    )

if __name__ == "__main__":
    main()
