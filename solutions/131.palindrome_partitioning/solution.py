from typing import List

class Solution:

    def find_recursive(self, s, tmp, ret):
        if not s:
            arr = tmp.split(',')
            arr.pop()
            ret.append(arr)
            return

        for i in range(1, len(s) + 1):
            part = s[:i]
            a, b = 0, len(part) - 1
            is_palindrome = True
            while a < b:
                if part[a] != part[b]:
                    is_palindrome = False
                    break
                else:
                    a += 1
                    b -= 1
            if is_palindrome:
                new_str = s[i:]
                self.find_recursive(new_str, tmp + part + ',', ret)

    def partition(self, s: str) -> List[List[str]]:
        ret = []
        self.find_recursive(s, '', ret)
        return ret


if __name__ == '__main__':
    s = Solution()

    print(s.partition("aabaa"))
