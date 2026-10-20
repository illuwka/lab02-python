def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def main():
    print("=== Калькулятор: Цельсій -> Кельвін ===")
    try:
        celsius = float(input("Введіть температуру в °C: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C = {kelvin:.2f} K")
    except ValueError:
        print("Помилка: введіть числове значення!")


if __name__ == "__main__":
    main()