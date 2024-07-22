class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        language = {order[i]: i for i in range(26)}
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            for j in range(len(first)):
                if j == len(second):
                    return False
                if language[first[j]] < language[second[j]]:
                    break
                if language[first[j]] > language[second[j]]:
                    return False

        return True
