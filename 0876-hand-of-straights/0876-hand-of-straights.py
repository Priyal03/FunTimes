class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            card = minHeap[0]
            for x in range(groupSize):
                if count[x + card] == 0:
                    return False
                count[x + card] -= 1
                if count[x + card] == 0:
                    topelement = heapq.heappop(minHeap)
                    if x + card != topelement:
                        return False
        return True
