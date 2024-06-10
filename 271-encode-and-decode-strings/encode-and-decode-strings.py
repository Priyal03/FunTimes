class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for s in strs:
            encoded += str(len(s))+';'+s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i=0
        print(s)
        while i < (len(s)):
            start = s.find(';',i)
            length = int(s[i:start])
            start+=1
            end = start+length
            curr = s[start:end]
            decoded.append(curr)
            i=end
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))