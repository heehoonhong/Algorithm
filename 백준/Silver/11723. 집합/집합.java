//package ctp;

import java.io.*;
import java.util.*;


public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		Queue<Integer> queue=new LinkedList<>();
		StringTokenizer st;
		
		int m=Integer.parseInt(br.readLine());
		
		
		for(int i = 0;i<m;i++) {
			String l=br.readLine();
			st=new StringTokenizer(l);
			String calc=st.nextToken();
			if(st.hasMoreTokens()) { // 그 외 경우
				int num=Integer.parseInt(st.nextToken());
				if(calc.equals("add")) {
					if(queue.contains(num)) {
						continue;
					}
					else {
						queue.offer(num);
					}
				}
				else if(calc.equals("remove")) {
					if(queue.contains(num)) {
						queue.remove(num);
					}
					else {
						continue;
					}
				}
				else if(calc.equals("check")) {
					if(queue.contains(num)) {
						bw.write(1+"\n");
					}
					else {
						bw.write(0+"\n");
					}
				}
				else if(calc.equals("toggle")) {
					if(queue.contains(num)) {
						queue.remove(num);
					}
					else {
						queue.offer(num);
					}
				}
			}
			else { // all,empty 인 경우
				if(calc.equals("all")) {
					queue.clear();
					for(int j = 1;j<=20;j++) {
						queue.offer(j);
					}
				}
				else if(calc.equals("empty")) {
					queue.clear();
				}
			}
			
			
		}
		br.close();
		bw.flush();
		bw.close();
	}
}
