class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)
        
        arr = [(-count, word) for word,count in freq.items()]
        # for word, count in freq.items():
        #     heappush(arr, (-count, word))
        
        heapify(arr)

        return [heappop(arr)[1] for _ in range(k)]