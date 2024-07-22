class Solution:
    def minimumLength(self, s: str) -> int:
        temp = s
        abcd = defaultdict(deque)
        for i in range(len(s)):
            abcd[s[i]].append(i)

        count = 0
        for c, occur in abcd.items():
            while len(occur)>2:
                # print(occur)
                occur.popleft()
                occur.pop()
                # print(occur)
                count+=2

        return len(s)-count 