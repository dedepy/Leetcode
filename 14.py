#https://leetcode.com/problems/longest-common-prefix/description/
from typing import List


class Solution:
    #Декоратор @staticmethod делает метод независимым от экземпляра класса.
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        if not strs:
            return ""

        # Берем первый элемент как возможный префикс
        prefix = strs[0]

        # Сравниваем префикс с каждым словом в массиве
        for word in strs[1:]:
            # Укорачиваем префикс до тех пор, пока он не станет частью текущего слова
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))