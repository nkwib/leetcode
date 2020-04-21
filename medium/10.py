class Solution:
    def isMatch(self, s, p):
        subPatterns = []
        strSubPattern = [(s, 0)]
        seen = {(s, 0)}
        
        def markSeen(string, index):
            if (string, index) not in seen:
                seen.add((string, index))
                strSubPattern.append((string, index))

        for i in p:
            if i == '*': subPatterns[-1] += '*'
            else: subPatterns.append(i)
            
        while strSubPattern:
            s, ind = strSubPattern.pop()
            if ind == len(subPatterns):
                if not s: return True
                else: continue
            subptn = subPatterns[ind]
            if subptn == '.*':
                for i in range(len(s)+1):
                    markSeen(s[i:], ind+1)
            elif subptn.endswith('*'):
                firstChar = subptn[0]
                for i in range(len(s)+1):
                    if s.startswith(firstChar*i): markSeen(s[i:], ind+1)
                    else: break
            elif subptn == '.' and s: markSeen(s[1:], ind+1)
            elif s.startswith(subptn): markSeen(s[1:], ind+1)
        return False

print(Solution().isMatch("aab", "c*a*b"))