class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;//assuming all nodes are disjoined in the begining.

        UnionFind uf = new UnionFind(n);
        int totalDisjointSet = n;

        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(isConnected[i][j]==1 && uf.find(i) != uf.find(j)){
                    totalDisjointSet--;
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

    public int find(int x){
        if(parent[x]!=x){
            parent[x]=find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y){
        int xroot = find(x);
        int yroot = find(y);

        if(xroot == yroot)
            return;
        else if(rank[xroot] < rank[yroot]){
            parent[xroot] = yroot;
        }else if(rank[xroot]>rank[yroot]){
            parent[yroot]=xroot;
        }else{
            parent[yroot]=xroot;
            rank[xroot]++;
        }
        count--;
    }
}