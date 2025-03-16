class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Создаем массив строк для каждой строки зигзага
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Распределяем символы по строкам
        for char in s:
            rows[current_row] += char
            # Если достигли первой или последней строки, меняем направление
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Обновляем текущую строку
            current_row += 1 if going_down else -1

        # Собираем все строки вместе
        return ''.join(rows)
s = "PAYPALISHIRING"
numRows = 3
solution = Solution()
print(solution.convert(s, numRows))  # Вывод: "PAHNAPLSIIGYIR"