//package ctp;

import java.util.*;


public class Main {
	/*
	public Queue<Integer> solution(int n,int k) {
		
	}*/
	
	public static void main(String[] args) {
		Main T = new Main();
		Scanner sc=new Scanner(System.in);
		String inputBuffer="";
		while(true) {
			inputBuffer=sc.nextLine();
			if(inputBuffer.equals(".")) break;
		
			char[] ch=inputBuffer.toCharArray();
			Stack<Character> stack=new Stack<>();
			boolean isValid=true; // 올바른 괄호 여부
			
			for(int i = 0;i<ch.length;i++) {
				if(ch[i]=='('||ch[i]=='[') {
					stack.push(ch[i]);
				}
				else if(ch[i]==')') {
					if(stack.isEmpty()) {
						isValid=false;
						break;
					}
					else {
						if(stack.peek()=='(') stack.pop();
						else {
							isValid=false;
							break;
						}
					}
				}
				else if(ch[i]==']') {
					if(stack.isEmpty()) {
						isValid=false;
						break;
					}
					else {
						if(stack.peek()=='[') stack.pop();
						else {
							isValid=false;
							break;
						}
					}
				}
			}
			if(isValid&&stack.isEmpty()) System.out.println("yes");
			else System.out.println("no");
			
		}
	}

}
