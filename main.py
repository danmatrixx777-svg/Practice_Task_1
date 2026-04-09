import datetime

# Словарик для отрисовки цифр 5x3
DIGITS = {
    '0': ["*** ", "* * ", "* * ", "* * ", "*** "],
    '1': ["  * ", "  * ", "  * ", "  * ", "  * "],
    '2': ["*** ", "  * ", "*** ", "* ", "*** "],
    '3': ["*** ", "  * ", "*** ", "  * ", "*** "],
    '4': ["* * ", "* * ", "*** ", "  * ", "  * "],
    '5': ["*** ", "* ", "*** ", "  * ", "*** "],
    '6': ["*** ", "* ", "*** ", "* * ", "*** "],
    '7': ["*** ", "  * ", "  * ", "  * ", "  * "],
    '8': ["*** ", "* * ", "*** ", "* * ", "*** "],
    '9': ["*** ", "* * ", "*** ", "  * ", "*** "],
    ' ': ["    ", "    ", "    ", "    ", "    "]
}

def get_day_of_week(d, m, y):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[datetime.date(y, m, d).weekday()]

def is_leap(y):
    return "Да" if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else "Нет"

def calculate_age(d, m, y):
    today = datetime.date.today()
    birth = datetime.date(y, m, d)
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

def print_styled_date(date_str):
    # Рисуем по строкам (всего 5 строк в высоту)
    for i in range(5):
        line = ""
        for char in date_str:
            line += DIGITS[char] + "  "
        print(line)

def main():
    print("--- Программа анализа даты рождения ---")
    day = int(input("Введите день рождения (дд): "))
    month = int(input("Введите месяц (мм): "))
    year = int(input("Введите год (гггг): "))

    print(f"\nДень недели: {get_day_of_week(day, month, year)}")
    print(f"Високосный год: {is_leap(year)}")
    print(f"Ваш возраст: {calculate_age(day, month, year)} лет")
    
    print("\nДата в стиле электронного табло:")
    # Формируем строку дд мм гггг
    formatted_date = f"{day:02d} {month:02d} {year}"
    print_styled_date(formatted_date)

if __name__ == "__main__":
    main()