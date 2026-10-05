class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(start,current,total):
            if total == target:
                ans.append(current[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                backtrack(i,current,total+candidates[i])
                current.pop()
        backtrack(0,[],0)
        return ans