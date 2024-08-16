class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique = set()

        for email in emails:
            
            localName, domainName=email.split('@')
            #print((localName+'@'+domainName))
            
            name = localName.split('+')[0].replace('.','')
            #print((name+'@'+domainName))not consider anything after + sign and replace . with null
            
            unique.add((name+'@'+domainName))
            
        return len(unique)
    