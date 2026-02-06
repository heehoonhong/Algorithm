import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        List<String> phones=Arrays.asList(phone_book);
        Collections.sort(phones);
        boolean flag=true;
        for(int i=0;i<phones.size()-1;i++){
            if(phones.get(i+1).indexOf(phones.get(i))==0){
                flag=false;
            }
        }
        if(flag==false){
            return false;
        }
        else{
            return true;
        }
    }
}