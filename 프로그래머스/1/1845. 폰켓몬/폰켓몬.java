import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> animals=new HashSet<>();
        for(int num:nums){
            animals.add(num);
        }
        return Math.min(animals.size(),nums.length/2);
        
    }
}