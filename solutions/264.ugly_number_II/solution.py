class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        a, b, c = 0, 0, 0
        i = 0
        while i < n:
            can_a = 2 * arr[a]
            can_b = 3 * arr[b]
            can_c = 5 * arr[c]

            next_e = min(can_a, can_b, can_c)

            if next_e == can_a:
                a += 1
            elif next_e == can_b:
                b += 1
            else:
                c += 1

            if next_e in arr:
                continue
            arr.append(next_e)
            i += 1
        return arr[n - 1]


