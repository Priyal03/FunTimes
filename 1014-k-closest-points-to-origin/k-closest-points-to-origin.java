class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Map<Integer,Double> map = new HashMap<Integer,Double>();
        int result[][]=new int[k][2];

        for(int i=0;i<points.length;i++){
            double dis = Math.sqrt(Math.pow(points[i][0], 2)+Math.pow(points[i][1],2));
            map.put(i,dis);
        }

        List<Map.Entry<Integer,Double>> sortedlist = new ArrayList<>(map.entrySet());
        Collections.sort(sortedlist, new Comparator<Map.Entry<Integer,Double>>(){
            public int compare(Map.Entry<Integer,Double> a, Map.Entry<Integer,Double> b){
                return a.getValue().compareTo(b.getValue());
            }
        });//you are sorting in increasing order of the distance, so that's all we need to get the correct mapping from points 2D array.

        for(int i=0;i<k;i++){
            result[i][0]=points[sortedlist.get(i).getKey()][0];
            result[i][1]=points[sortedlist.get(i).getKey()][1];
        }
        return result;
    }
}