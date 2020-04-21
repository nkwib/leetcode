from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def isOdd(num: int):
            return len(str(num))%2 == 0
        count: int = 0
        for n in nums:
            if isOdd(n): count += 1
        return count

Solution().findNumbers([23,15,2,2,631,24])