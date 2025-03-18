class Solution:
    def reverse(self, x: int) -> int:
        # Определяем пределы 32-битного целого числа
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # Сохраняем знак числа
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        # Переворачиваем число
        reversed_num = 0
        while x_abs != 0:
            last_digit = x_abs % 10
            reversed_num = reversed_num * 10 + last_digit
            x_abs //= 10

        # Возвращаем результат с учетом знака
        reversed_num *= sign

        # Проверяем, не выходит ли число за пределы диапазона
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num

x = int(input())
solution = Solution()
print(solution.reverse(x))