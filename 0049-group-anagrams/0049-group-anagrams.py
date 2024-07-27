class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #["eat","tea","tan","ate","nat","bat"]
        anagramStore=defaultdict(list)
        for word in strs:
            count=[0]*26
            for i in word:
                count[ord(i)-ord('a')]+=1
            anagramStore[tuple(count)].append(word)
        return anagramStore.values()