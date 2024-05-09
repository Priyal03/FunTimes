class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}

        for word in strs:
            sort = str(sorted(word))
            if sort in map:
                map[sort].append(word)
            else:
                map[sort]=[word]

        return map.values()