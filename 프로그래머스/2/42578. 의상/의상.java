import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String,Integer> wear=new HashMap<>();
        for(int i = 0;i<clothes.length;i++){
            wear.put(clothes[i][1],wear.getOrDefault(clothes[i][1],0)+1);
        }
        int answer=1;
        for(Map.Entry<String,Integer> entrySet:wear.entrySet()){
            answer*=(entrySet.getValue()+1);
        }
        return answer-1;
    }
}