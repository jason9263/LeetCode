class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            tmp_quote = 1
            while tmp_quote * divisor <= dividend:
                tmp_quote = tmp_quote << 1
            tmp_quote = tmp_quote >> 1
            dividend -= tmp_quote * divisor
            ans += tmp_quote

        return ans*sign
