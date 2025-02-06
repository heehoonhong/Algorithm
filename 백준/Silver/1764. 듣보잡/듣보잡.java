//package ctp;

import java.util.*;


public class Main {
	/*
	public Queue<Integer> solution(int n,int k) {
		
	}
	*/
	public static void main(String[] args) {
		Main T = new Main();
		Scanner sc=new Scanner(System.in);
		int n= sc.nextInt(); 
		int m=sc.nextInt();
		
		sc.nextLine();
		
		Set<String> listen = new HashSet<>();
		Set<String> see=new HashSet<>();
		List<String> answer=new ArrayList<>();
		
		for(int i = 0;i<n;i++) {
			listen.add(sc.nextLine());
		}
		for(int i = 0;i<m;i++) {
			see.add(sc.nextLine());
		}
		
		
		
		for(String element:listen) {
			if(see.contains(element)) answer.add(element);
		}
		
		Collections.sort(answer);
		System.out.println(answer.size());
		for(String element:answer) {
			System.out.println(element);
		}
		
		
	}

}
