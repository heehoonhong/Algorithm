import java.util.*;

class Solution {
    public static class Price{
        int price;
        int index;
        public Price(int price,int index){
            this.price=price;
            this.index=index;
        }
    }
    
    public int[] solution(int[] prices) {
        Stack<Price> stack=new Stack<>();
        int[] result=new int[prices.length];
        stack.add(new Price(prices[0],0));
        for(int i = 1;i<prices.length;i++){
            if(stack.peek().price<=prices[i]){
                stack.add(new Price(prices[i],i));
            }
            else{
                while(!stack.isEmpty() && stack.peek().price>prices[i]){
                    result[stack.peek().index]=i-stack.peek().index;
                    stack.pop();
                }
                stack.add(new Price(prices[i],i));
            }
        }
        if(!stack.isEmpty()){
            Price[] ss=new Price[stack.size()];
            for(int i=stack.size()-1;i>=0;i--){
                Price price2=stack.pop();
                ss[i]=price2;
            }
            for(int i = 0;i<ss.length;i++){
                result[ss[i].index]=(ss[ss.length-1].index)-(ss[i].index);
            }
        
        }
        return result;
        
    }
}