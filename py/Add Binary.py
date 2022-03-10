class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


a = bin(1)

print(a.zfill(10))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        ans = []

        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1

            if b[i] == '1':
                carry += 1

            ans.append(str(carry % 2))
            carry = carry // 2

        if carry == 1:
            ans.append('1')

        ans.reverse()

        return ''.join(ans)
