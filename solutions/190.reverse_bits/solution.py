BITS = 32


class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(BITS):
            mask = 1 << i
            val_mask = 1 << BITS - i - 1
            if mask & n == mask:
                ret += val_mask
        return ret


