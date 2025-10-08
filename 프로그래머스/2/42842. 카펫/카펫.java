class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0,0};
        int total=brown+yellow;
        int width,height;
        
        for(width=total;width>=1;width--){
            height=total/width;
            if(total%width==0){
                if((width-2)*(height-2)==yellow){
                    answer[1]=width;
                    answer[0]=height;
                }
            }
        }
        
        
        
        return answer;
    }
}