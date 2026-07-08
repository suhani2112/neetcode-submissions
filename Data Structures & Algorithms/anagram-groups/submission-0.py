class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for st in strs:
            count = [0]*26

            for c in st:
                count[ord(c)-ord('a')] += 1
            
            key = tuple(count)
            map[key].append(st)
        return list(map.values())
        