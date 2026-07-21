class Solution:
    def isValid(self, s: str) -> bool:
        di = dict(('()','{}','[]'))
        stack = []

        for char in s :
            if char in '({[':
                stack.append(char)
            elif len(stack) == 0 or char != di[stack.pop()]:
                return False
        return len(stack) == 0 