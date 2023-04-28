class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            
            map.put(num, map.getOrDefault(num,0)+1);
        }
        
        PriorityQueue<Integer> que = new PriorityQueue<>((a,b) -> map.get(b)-map.get(a)); 
        //this is called reverse order comparision which sorts elements in decending order.
        //condition to compare is defined under comparator or comparable interface
        
        //then queue helps in storing whichever object we need.
        que.addAll(map.keySet()); //add only the key set after sorting is performed. 
        
        int[] ans = new int[k]; int pos=0;
        
        while(k-->0){
            
            ans[pos++]=que.remove();
        }
        
        return ans;
    }
}