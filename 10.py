class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Создаем таблицу DP
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Базовый случай: пустая строка соответствует пустому шаблону
        dp[0][0] = True

        # Инициализация первой строки для случаев с '*'
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Заполняем таблицу
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Текущие символы совпадают или шаблон содержит '.'
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' может быть нулевым количеством раз
                    dp[i][j] = dp[i][j - 2]
                    # Или '*' может продолжать предыдущий символ
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[len(s)][len(p)]

s = "ab"
p = "a*b*"
solution = Solution()
print(solution.isMatch(s, p))  # Вывод: False