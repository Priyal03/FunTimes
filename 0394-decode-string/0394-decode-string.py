class Solution:
    index=0
    def decodeString(self, s: str) -> str:
        result=[]
        
        while self.index<len(s):
            if s[self.index]==']':
                break
            if s[self.index].isalpha():
                result.append(s[self.index])
                self.index+=1
            else:
                digit=0
                while self.index<len(s) and s[self.index].isdigit():
                    digit=digit*10+int(s[self.index])
                    self.index+=1
                self.index+=1
                decoded=self.decodeString(s)
                result.append(decoded*digit)
                self.index+=1
        
        return ''.join(result)

        #redo this!!!! 