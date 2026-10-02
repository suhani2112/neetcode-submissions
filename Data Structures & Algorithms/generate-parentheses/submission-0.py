class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtracks(s,open,close):
            if len(s)== 2*n:
                result.append(s)
                return
            if open<n:
                backtracks(s + "(",open+1, close)
            if close<open:
                backtracks(s+")",open,close+1)
        backtracks("",0,0)
        return result
        