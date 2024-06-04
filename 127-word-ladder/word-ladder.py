from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wset = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            word, path = queue.popleft()
            if word == endWord:
                return path
            for i in range(len(word)):
                for c in ascii_lowercase:
                    newword = word[:i] + c + word[i + 1 :]
                    if newword in wset:
                        wset.remove(newword)
                        queue.append((newword, path + 1))
        return 0
