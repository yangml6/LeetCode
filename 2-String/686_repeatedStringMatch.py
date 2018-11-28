class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenA = len(A)
        lenB = len(B)
        time1 = lenB // lenA
        for i in range(time1, time1+lenA):
            if B in A * i:
                return i
        return -1

    def repeatedStringMatch2(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i) : return q+i
        return -1
    # Rolling Hash
    def repeatedStringMatch3(self, A, B):
        def check(index):
            return all(A[(i + index) % len(A)] == x for i, x in enumerate(B))
        q = (len(B) - 1) // len(A) + 1
        p, MOD = 113, 10**9 + 7
        p_inv = pow(p, MOD-2, MOD)
        power = 1

        b_hash = 0
        for x in map(ord, B):
            b_hash += power * x
            b_hash %= MOD
            power = (power * p) % MOD

        a_hash = 0
        power = 1
        for i in range(len(B)):
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            power = (power * p) % MOD

        if a_hash == b_hash and check(0) : return q
        
        power = (power * p_inv) % MOD
        for i in range(len(B), (q+1)*len(A)):
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i-len(B) + 1):
                return q if i < q * len(A) else q+1
        return -1





sol = Solution()
A = 'abc'
B = 'cabcabcab'
ans = sol.repeatedStringMatch3(A, B)
print(ans)