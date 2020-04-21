class Solution:
    def balancedStringSplit(self, s: str) -> int:
        finalRes = 0
        balance = 0
        for i in range(len(s)):
            s, last = s[:-1], s[-1]
            if last == 'L': balance += 1
            else: balance -= 1
            if balance == 0: finalRes += 1
        return finalRes







s = "RLRRLLRLRL"
print(Solution().balancedStringSplit(s))