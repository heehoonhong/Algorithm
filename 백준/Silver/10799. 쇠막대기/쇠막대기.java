//package ctp;

import java.util.*;


public class Main {

	public int solution(String str){
		int answer=0;
		Stack<Character> stack=new Stack<>();
		char[] ch=str.toCharArray();
		for(int i = 0;i<ch.length;i++) {
			if(ch[i]=='(') {
				stack.push(ch[i]);
			}
			else {
				if(ch[i-1]=='(') {
					stack.pop();
					answer+=stack.size();
				}
				else {
					answer++;
					stack.pop();
				}
			}
		}
		
		
		return answer;
	}
	
	public static void main(String[] args) {
		Main T = new Main();
		Scanner kb=new Scanner(System.in);
		String str=kb.nextLine();
		System.out.println(T.solution(str));
	}

}
