import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] first={1,2,3,4,5};
        int[] second={2,1,2,3,2,4,2,5};
        int[] third={3,3,1,1,2,2,4,4,5,5};
        int[] score=new int[3];
        
        for(int i = 0;i<answers.length;i++){
            if(answers[i]==first[i%5]) score[0]++;
            if(answers[i]==second[i%8]) score[1]++;
            if(answers[i]==third[i%10]) score[2]++;
        }
        
        int maxScore=Math.max(score[0],Math.max(score[1],score[2]));
        
        List<Integer> answerList=new ArrayList<>();
        for(int i=0;i<3;i++){
            if(maxScore==score[i]) answerList.add(i+1);
        }
        int[] answer=new int[answerList.size()];
        for(int i=0;i<answerList.size();i++){
            answer[i]=answerList.get(i);
        }
        //return answerList.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}