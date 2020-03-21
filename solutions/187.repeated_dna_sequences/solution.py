from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        tmp, ret = set(), set()
        index = 10
        while index <= len(s):
            part = s[index - 10:index]
            if part in tmp:
                ret.add(part)
            else:
                tmp.add(part)
            index += 1
        return list(ret)
