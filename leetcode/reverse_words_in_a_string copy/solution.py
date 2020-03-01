class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        ret = []

        s = s.strip()

        for c in s:
            if c.isspace():
                if len(arr) > 0:
                    ret.append(''.join(arr))
                    arr.clear()
            else:
                arr.append(c)
        if len(arr) > 0:
            ret.append(''.join(arr))
            arr.clear()
        ret.reverse()
        return " ".join(ret)


