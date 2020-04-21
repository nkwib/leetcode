class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #map = {}
        #for i in range(len(J)):
        #    map[J[i]] = 0
        count = 0
        for i in range(len(S)):
            if str([S[i]][0]) in J: count +=1
        return count


J = "aAB"
S = "aAAbbbb"
print(Solution().numJewelsInStones(J, S))