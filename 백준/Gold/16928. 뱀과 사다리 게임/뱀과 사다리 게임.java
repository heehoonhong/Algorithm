//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	static int[][] ladder;
	static int[][] snake;
	static int[] board;
	static int[] visited;
	static Queue<Integer> queue=new LinkedList<>();
	static int n,m;
	static BufferedWriter bw;
	
	public static int dice() {
		return (int)(Math.random()*6)+1;
	}
	
	public static void BFS() throws IOException {
		while(!queue.isEmpty()) {
			int temp=queue.poll();
			
			for(int diceNum=1;diceNum<=6;diceNum++) {
				int nextNum=temp+diceNum;
				
				if(nextNum>100) continue;
				
				for(int i = 0;i<n;i++) {
					if(nextNum==ladder[i][0]) {
						nextNum=ladder[i][1];
						break;
					}
				}
				
				for(int i = 0;i<m;i++) {
					if(nextNum==snake[i][0]) {
						nextNum=snake[i][1];
						break;
					}
				}
				
				if(visited[nextNum]==0) {
					visited[nextNum]=1;
					board[nextNum]=board[temp]+1;
					queue.offer(nextNum);
				}
				
				if(nextNum==100) return;
			}
		}
	}
	

	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		bw= new BufferedWriter(new OutputStreamWriter(System.out));
    
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		n=Integer.parseInt(st.nextToken());
		m=Integer.parseInt(st.nextToken());
		
		ladder=new int[n][2];
		snake=new int[m][2];
		board=new int[101];
		visited=new int[101];
		
		// 사다리의 정보 입력하기
		for(int i = 0;i<n;i++) {
			String l=br.readLine();
			st=new StringTokenizer(l);
			int x=Integer.parseInt(st.nextToken());
			int y=Integer.parseInt(st.nextToken());
			ladder[i][0]=x;
			ladder[i][1]=y;
		}
		
		// 뱀의 정보 입력하기
		for(int i = 0;i<m;i++) {
			String l=br.readLine();
			st=new StringTokenizer(l);
			int u=Integer.parseInt(st.nextToken());
			int v=Integer.parseInt(st.nextToken());
			snake[i][0]=u;
			snake[i][1]=v;
		}
		
		queue.offer(1);
		visited[1]=1;
		BFS();
		bw.write(board[100]+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
