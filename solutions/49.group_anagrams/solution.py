class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp = dict()

        for s in strs:
            val = ''.join(sorted(s))
            if val in tmp:
                tmp[val].append(s)
            else:
                tmp[val] = [s]
        ret = []
        for k in tmp:
            ret.append(tmp[k])
        return ret

    def get_val(self, param, range_list):
        ret = 0
        for i in param:
            ret += range_list[ord(i) - ord('a')]
        return ret

