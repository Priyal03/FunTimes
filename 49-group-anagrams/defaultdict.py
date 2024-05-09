class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)

        for word in strs:
            sort = str(sorted(word))
            map[sort].append(word)     

        return map.values()
