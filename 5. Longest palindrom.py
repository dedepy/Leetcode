class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            # Расширяемся влево и вправо, пока символы совпадают
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Возвращаем найденный палиндром
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            # Нечетная длина палиндрома (центр — один символ)
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Четная длина палиндрома (центр — два символа)
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

s = "abad"
solution = Solution()
print(solution.longestPalindrome(s))  # Вывод: "bab" или "aba"