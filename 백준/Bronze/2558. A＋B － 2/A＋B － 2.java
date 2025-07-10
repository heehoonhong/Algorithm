//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		int a=Integer.parseInt(br.readLine());
		int b=Integer.parseInt(br.readLine());
		
		bw.write(a+b+"\n");
		br.close();
		bw.flush();
		bw.close();
	}
}
