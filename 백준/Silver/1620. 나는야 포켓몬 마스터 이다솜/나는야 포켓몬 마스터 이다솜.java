//package ctp;

import java.io.*;
import java.util.*;


public class Main {
   
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st=new StringTokenizer(br.readLine());
		
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		Map<String,Integer> pokes=new HashMap<>();
		Map<Integer,String> pokesReverse=new HashMap<>();
		
		for(int i = 0;i<n;i++) {
			String poke=br.readLine();
			pokes.put(poke, pokes.getOrDefault(poke, 0)+(i+1));
			pokesReverse.put(i+1,poke );
		}
		
		for(int i = 0;i<m;i++) {
			String line=br.readLine();
			if(Character.isAlphabetic(line.charAt(0))){
				bw.write(pokes.get(line)+"\n");
			}
			else {
				int dd=Integer.parseInt(line);
				bw.write(pokesReverse.get(dd)+"\n");
			}
		}
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	
}

