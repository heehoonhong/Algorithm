import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int hIndex=0;
        int cl=citations.length;
        for(int h = 0;h<citations.length;h++){
            if(citations[h]>=cl-h){
                hIndex=cl-h;
                break;
            }
        }
        return hIndex;
    }
}