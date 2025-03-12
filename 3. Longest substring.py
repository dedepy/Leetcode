class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Хранит последний индекс каждого символа
        max_length = 0  # Максимальная длина подстроки
        left = 0  # Левый указатель окна

        for right, char in enumerate(s):
            # Если символ уже встречался, двигаем левый указатель
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            # Обновляем индекс символа
            char_index_map[char] = right

            # Обновляем максимальную длину
            max_length = max(max_length, right - left + 1)

        return max_length
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))