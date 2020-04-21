from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        def slice_per(source, step):
            for i in range(0, len(source), step):  
                yield source[i:i + step]
        groups = {}
        res = []
        for index, person in enumerate(groupSizes, start=0):
            if person in groups.keys(): groups[person].append(index) 
            else: groups[person] = [index]
        for k in groups.keys():
                group = list(slice_per(groups[k], k))
                res.extend(group)
        return res



groupSizes = [3,3,3,3,4,4,2,2,4,3,4,3,1]
print(Solution().groupThePeople(groupSizes))