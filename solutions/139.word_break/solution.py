from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = set(wordDict)

        tmp = [False for _ in range(len(s))]

        for i in range(0, len(s)):
            for j in range(-1, i):
                if j == -1 or tmp[j]:
                    if s[j + 1:i + 1] in cache:
                        tmp[i] = True
                        break

        return tmp[len(s) - 1]
