class Solution:

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True for _ in range(n)]
        is_prime[0] = False
        is_prime[1] = False

        bound = int(n ** 0.5)
        for i in range(2, bound + 1):
            if not is_prime[i]:
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False
        return sum(is_prime)



if __name__ == '__main__':
    s = Solution()

    print(s.countPrimes(10))
