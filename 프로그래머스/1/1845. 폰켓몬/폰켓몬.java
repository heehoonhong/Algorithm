import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Map<Integer,Integer> animals=new HashMap<Integer,Integer>();
        for(int num:nums){
            animals.put(num,animals.getOrDefault(num,0)+1);
        }
        
        return Math.min(animals.size(),nums.length/2);
    }
}