class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_positive = (numerator >= 0 and denominator >= 0) or (numerator < 0 and denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        base, decimal = divmod(numerator, denominator)

        symbol = ''
        if not is_positive:
            symbol = '-'

        decimals = []
        cache = dict()
        decimal *= 10
        while decimal > 0:
            if decimal in cache:
                index = cache[decimal]
                return '{}{}.{}({})'.format(symbol, base, ''.join(str(x) for x in decimals[:index]),
                                            ''.join(str(x) for x in decimals[index:]))
            div, mod = divmod(decimal, denominator)
            decimals.append(div)

            cache[decimal] = len(decimals) - 1

            decimal = mod * 10

        if decimals:
            return '{}{}.{}'.format(symbol, base, ''.join(str(x) for x in decimals))

        if base == 0:
            return str(base)
        return "{}{}".format(symbol, base)

