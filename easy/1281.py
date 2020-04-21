class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        spl = [int(x) for x in str(n)]
        add = 0
        mlt = 1
        for d in spl:
            mlt = mlt * d
            add += d
        return mlt-add


print(Solution().subtractProductAndSum(4421))