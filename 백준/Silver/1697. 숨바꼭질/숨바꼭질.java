//package ctp;

import java.io.*;
import java.util.*;




public class Main {
	
	static Queue<Integer> queue=new LinkedList<>();
	static int[] visited;
	static BufferedWriter bw;
	static int n,m;
	
	public static void BFS(int m) throws Exception{
		while(!queue.isEmpty()) {
			int temp=queue.poll();
			
			for(int i = 0;i<3;i++) {
				int nx;
				if(i==0) {
					nx=temp-1;
				}
				else if(i==1) {
					nx=temp+1;
				}
				else {
					nx=temp*2;
				}
				
				if(nx>=0&&nx<=100000&&visited[nx]==0) {
					visited[nx]=visited[temp]+1;
					queue.offer(nx);
				}
				if(nx==m) {
					bw.write(visited[nx]+"\n");
					return;
				}
			}
		}
	}
	
	
    public static void main(String[] args) throws Exception {

    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	n=Integer.parseInt(st.nextToken());
    	m=Integer.parseInt(st.nextToken());
    	
    	if (n == m) { // 시작 위치와 목표 위치가 같으면 0 출력
    		bw.write("0\n");
    		bw.flush();
    		bw.close();
    		br.close();
    		return;
    	}

    	
    	visited=new int[100001];
    	queue.offer(n);
    	visited[n]=0;
    	BFS(m);
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
