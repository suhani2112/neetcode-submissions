class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        left = 0
        right = 0
        totalwater = 0

        while i < j:
            left = max(left,height[i])
            right = max(right,height[j])

            if left < right :
                totalwater += left - height[i]
                i += 1
            else:
                totalwater += right - height[j]
                j -= 1
        return totalwater