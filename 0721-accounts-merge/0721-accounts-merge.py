class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        n=len(accounts)
        emails_to_user={}
        email_group_by_user={}
        result=[]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx!=rooty:
                parent[rootx]=rooty
        
        def find(x):
            if x not in parent:
                parent[x]=x
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        for i in range(n):
            for email in accounts[i][1:]:
                if email in emails_to_user:
                    #perform union operation for those index numbers of repeating emails
                    union(i,emails_to_user[email])
                else:
                    emails_to_user[email]=i
        # print(emails_to_user)
        #still using the index number to map as they are unique and names could be repeating.
        for email, i in emails_to_user.items():
            user = find(i)
            if user not in email_group_by_user:
                email_group_by_user[user]=set()  
            email_group_by_user[user].add(email)
                
        # print(email_group_by_user)
        #at very last, we will put user names from that index in accounts input matrix
        for i, emails in email_group_by_user.items():
            result.append([accounts[i][0]]+sorted(emails))

        return result
            