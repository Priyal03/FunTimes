class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        tmap = {}
        
        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]]!=t[i]:
                return False
            mapping[s[i]]=t[i]

            if t[i] in tmap and tmap[t[i]]!=s[i]:
                return False
            tmap[t[i]]=s[i]
        
        return len(mapping)==len(tmap)