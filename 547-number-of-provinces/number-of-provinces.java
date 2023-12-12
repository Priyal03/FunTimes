class Solution {
    public int findCircleNum(int[][] isConnected) {
        //assuming all nodes are disjoined in the begining. 
        int n = isConnected.length;
        UnionFind uf = new UnionFind(n);
        
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(isConnected[i][j]==1 && uf.findParent(i) != uf.findParent(j)){
                    uf.union(i,j);
                }
            }
        }
        return uf.count;
    }
}

class UnionFind{
    int parent[];
    int rank[];
    int count;

    public UnionFind(int n){
        parent = new int[n];
        rank = new int[n];
        count=n;
        while(n-->0){
            parent[n]=n;
        }
    }

    public int findParent(int x){
        if(parent[x]!=x){
            parent[x]=findParent(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y){
        int xroot = findParent(x);
        int yroot = findParent(y);

        if(xroot == yroot)
            return;
        else if(rank[xroot] < rank[yroot]){
            parent[xroot] = yroot;
        }else if(rank[xroot]>rank[yroot]){
            parent[yroot]=xroot;
        }else{
            parent[xroot]=yroot;
            rank[yroot]++;
        }
        count--;
    }
}