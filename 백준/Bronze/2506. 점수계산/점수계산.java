import java.util.*;

public class Main {

	public int solution(int n,int[] arr){
		int answer=0;
		int count=0;
		
		
		
		for(int i = 0;i<n;i++) {
			if(arr[i]==0) {
				count=0;
			}
			else {
				count++;	
				answer+=count;
			}
					
		}
		return answer;
	}
	
	public static void main(String[] args) {
		Main T = new Main();
		Scanner kb=new Scanner(System.in);
		int n=kb.nextInt();
		int[] arr=new int[n];
		for(int i = 0;i<n;i++) {
			arr[i]=kb.nextInt();
		}
		System.out.println(T.solution(n, arr));
		
	}

}