import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        // 변수명 오타 수정: stockPeried -> stockPeriod
        int[] stockPeriod = new int[prices.length];
        
        for (int i = 0; i < prices.length; i++) {
            // j는 마지막 인덱스까지 확인해야 함
            for (int j = i + 1; j < prices.length; j++) {
                // 1. 일단 1초가 흘렀으므로 기간을 1 증가시킴
                stockPeriod[i]++;
                
                // 2. 만약 현재 가격이 다음 가격보다 비싸면(가격 하락)
                if (prices[i] > prices[j]) {
                    // 3. 더 이상 확인할 필요가 없으므로 반복을 중단(break)
                    break;
                }
            }
        }
        return stockPeriod;
    }
}