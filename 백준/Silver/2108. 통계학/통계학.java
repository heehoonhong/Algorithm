//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        sc.nextLine();
        
        int[] arr=new int[n];
        int[] frequencies=new int[8001];
        
        int max=Integer.MIN_VALUE;
        int min=Integer.MAX_VALUE;
        int maxCount=0;
        int maxFreqNum=0;
        int sum=0;
        
        
        for(int i = 0;i<n;i++) {
        	arr[i]=sc.nextInt();
        	sum+=arr[i];
        	max=Math.max(max, arr[i]);
        	min=Math.min(min, arr[i]);
        	frequencies[arr[i]+4000]++;
        }
        
        // maxCount 찾기(최빈값을 찾는 과정)
        for(int i = 0;i<8001;i++) {
        	if(maxCount<frequencies[i]) {
        		maxCount=frequencies[i];
        		maxFreqNum=i-4000;
        	}
        }
        
        int freqCount=0;
        // maxCount를 통한 maxFreqNum(최빈값) 찾기
        
        
        
        for(int i = 0;i<8001;i++) {
        	if(maxCount==frequencies[i]) { 
        		// 1이라는 것은 이미 한 번 찾은 상태에서
        		// 이제 2번째를 맞닥뜨린 것이여서 그럼
        		if(freqCount==1) {
        			maxFreqNum=i-4000;
        			break;
        		}
        		else {
        			freqCount++;
        		}
        	}
        }
        Arrays.sort(arr);
        
        double average=sum/(double)n;
        
        System.out.println(Math.round(average));
        System.out.println(arr[n/2]);
        System.out.println(maxFreqNum);
        System.out.println(max-min);
        
	}
	
	
        	
}
