class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        for i in range(n):
            l = i+1
            h = n-1
            temp = target - numbers[i]
            while l <= h :
                mid = l + (h-l) // 2
                if numbers[mid] == temp :
                    return [ i+1 , mid +1]
                elif numbers[mid] < temp :
                    l = mid +1
                else:
                    h = mid-1
        return []