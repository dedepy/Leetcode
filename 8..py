class Solution:
    def myAtoi(self, s: str) -> int:
        # Определяем пределы 32-битного целого числа
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # Удаляем ведущие пробелы
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        # Проверяем наличие знака
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Извлекаем цифры
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Проверяем на переполнение перед добавлением цифры
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            result = result * 10 + digit
            i += 1

        # Возвращаем результат с учетом знака
        return sign * result