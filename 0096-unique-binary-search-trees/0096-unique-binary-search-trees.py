class Solution:
    def numTrees(self, n: int) -> int:
        
        uniqueBST=[1]*(n+1)
            # for each ith node we can have multiple bst with root
            # eX : 1,2,3,4 then if ithNode is 3 , 
            # then bst can have 1 and 2 as root, hence we need to compute for each of the root
            # n= 4 total = unique[0]*unique[3]+unique[1]*unique[2]+unique[2]*unique[1]+unique[3]*unique[0]
        for nodes in range(2,n+1):
            
            total=0
            for root in range(1,nodes+1):
                
                total+=uniqueBST[root-1]*uniqueBST[nodes-root] #total at this node = total at left subtree * total at right subtree

            uniqueBST[nodes]=total

        return uniqueBST[n]