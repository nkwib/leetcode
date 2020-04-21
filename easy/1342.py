class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        temp = num
        while temp != 0:
            print(temp)
            if temp%2 == 0:
                count += 1
                temp = temp/2
            else:
                count += 1
                temp -= 1
        return count

s = Solution()
res = s.numberOfSteps(6)
print(res)