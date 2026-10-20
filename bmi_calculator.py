def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Повертає індекс маси тіла (ІМТ)."""
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def interpret_bmi(bmi: float) -> str:
    """Повертає категорію ІМТ за класифікацією ВООЗ."""
    if bmi < 16:
        return "Виражений дефіцит маси тіла"
    elif bmi < 18.5:
        return "Недостатня маса тіла"
    elif bmi < 25:
        return "Нормальна маса тіла"
    elif bmi < 30:
        return "Надлишкова маса тіла (перед ожирінням)"
    elif bmi < 35:
        return "Ожиріння I ступеня"
    elif bmi < 40:
        return "Ожиріння II ступеня"
    else:
        return "Ожиріння III ступеня"


def read_positive_float(prompt: str) -> float:
    """Запитує додатне число, поки користувач не введе коректне значення."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value <= 0:
                print("Значення має бути більше нуля. Спробуй ще раз.")
                continue
            return value
        except ValueError:
            print("Введи число, наприклад 72.5")


def main():
    print("=== Калькулятор індексу маси тіла (ІМТ) ===")
    weight = read_positive_float("Вага (кг): ")
    height = read_positive_float("Зріст (см): ")

    bmi = calculate_bmi(weight, height)
    print(f"\nТвій ІМТ: {bmi:.1f}")
    print(f"Категорія: {interpret_bmi(bmi)}")
    print("\nПримітка: ІМТ — орієнтовний показник і не враховує м'язову масу, вік та інші фактори.")


if __name__ == "__main__":
    main()
