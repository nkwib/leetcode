from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0: return res
        else:
            return ['()']

print(Solution().generateParenthesis(1))

()
()()        (())
()()()      (())()      ()(())      (()()) ((()))
()()()()    (())(())    ((()))()    ()((())) (()())() ()(()()) (((())))