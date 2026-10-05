class Solution:
    def checkValidString(self, s: str) -> bool:
        minopen = 0
        maxopen = 0
        for ch in s:
            if ch == '(':
                minopen += 1
                maxopen += 1
            elif ch == ')':
                minopen -= 1
                maxopen -= 1
            else : #'*':
                minopen -= 1
                maxopen += 1
            minopen = max(minopen , 0)
            if maxopen < 0 :
                return False
        return minopen ==0 