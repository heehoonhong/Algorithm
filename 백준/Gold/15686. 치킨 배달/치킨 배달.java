//package ctp;

import java.io.*;
import java.util.*;



public class Main {
	
	static class Point{
		int x;
		int y;
		Point(int x,int y) {
			this.x=x;
			this.y=y;
		}
	}
	
	public static int n,m,answer;
	public static int[][] map;
	public static List<Point> home=new ArrayList<>();
	public static List<Point> chicken=new ArrayList<>();
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		n=Integer.parseInt(st.nextToken());
		m=Integer.parseInt(st.nextToken());
		map=new int[n][n];
		
		for(int i = 0;i<n;i++) {
			line=br.readLine();
			st=new StringTokenizer(line);
			for(int j = 0;j<n;j++) {
				map[i][j]=Integer.parseInt(st.nextToken());
				if(map[i][j]==1) {
					home.add(new Point(i,j));
				}
				else if(map[i][j]==2) {
					chicken.add(new Point(i,j));
				}
			}
		}
		
		answer=Integer.MAX_VALUE;
		dfs(0,new ArrayList<>());
		bw.write(answer+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	public static void dfs(int currentChickenNum,List<Point> selectedChicken) {
		if(selectedChicken.size()+(chicken.size()-currentChickenNum)<m) return;
		
		if(currentChickenNum==chicken.size()) {
			if(selectedChicken.size()==m) {
				answer=Math.min(answer, calculateDistance(selectedChicken));
			}
			return;
		}
		
		
		selectedChicken.add(chicken.get(currentChickenNum));
		dfs(currentChickenNum+1,selectedChicken);
		selectedChicken.remove(selectedChicken.size()-1);
		
		dfs(currentChickenNum+1,selectedChicken);
	}
	
	public static int calculateDistance(List<Point> selectedChicken) {
		int sum=0;
		
		for(Point h: home) {
			int min=Integer.MAX_VALUE;
			for(Point c:selectedChicken) {
				int distance=Math.abs(h.x-c.x)+Math.abs(h.y-c.y);
				min=Math.min(min, distance);
			}
			sum+=min;
		}
		
		return sum;
	}
}
