class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch.isalnum():
                st.append(ch)

        ns = ''.join(st).lower()
        
        print(ns)
        res = ns[::-1]

        if ns==res:
            return True
        else:
            return False