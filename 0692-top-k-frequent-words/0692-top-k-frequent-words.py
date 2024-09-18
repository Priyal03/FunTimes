class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)
        
        # sortedf = sorted(freq, key=freq.get, reverse=True)

        sortedf = sorted(freq.keys(), key=lambda x:(-freq[x],x))

        return sortedf[:k]