//package ctp;

import java.io.*;
import java.util.*;

public class Main {

    public static int num;
    public static int maxCount;
    public static int[] arr;
    public static int[] selected;
    public static StringBuilder sb = new StringBuilder();
    public static Set<String> resultSet=new LinkedHashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);

        num = Integer.parseInt(st.nextToken());
        maxCount = Integer.parseInt(st.nextToken());

        arr = new int[num];
        selected = new int[maxCount];

        line = br.readLine();
        st = new StringTokenizer(line);
        for (int i = 0; i < num; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        dfs(0);
        
        for(String s:resultSet) {
        	System.out.println(s);
        }
        
        br.close();
    }

    public static void dfs(int currentCount) {
    	if(currentCount==maxCount) {
    		StringBuilder sb=new StringBuilder();
    		for(int element:selected) {
    			sb.append(element).append(" ");
    		}
    		//sb.append("\n");
    		resultSet.add(sb.toString());
    		return;
    	}
    	
    	for(int i = 0;i<num;i++) {
    		selected[currentCount]=arr[i];
    		dfs(currentCount+1);
    	}
    }
}
