class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items() , key = lambda x:x[1] , reverse = True )

        ans = []
        for i in range(k):
            ans.append(sorted_freq[i][0])
        return ans

        