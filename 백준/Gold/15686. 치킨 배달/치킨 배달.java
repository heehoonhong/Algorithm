//package ctp;

import java.io.*;
import java.util.*;



public class Main {
	
	static class Point{
		int x,y;
		Point(int x,int y){
			this.x=x;
			this.y=y;
		}
	}
	
	public static int maxChickenNum,mapRow;
	public static List<Point> homeList=new ArrayList<>();
	public static List<Point> chickenList=new ArrayList<>();
	public static List<Point> selectedChickenList=new ArrayList<>();
	public static int[][] map;
	public static int answer;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		
		mapRow=Integer.parseInt(st.nextToken());
		maxChickenNum=Integer.parseInt(st.nextToken());
		
		map=new int[mapRow][mapRow];
		
		for(int i = 0;i<mapRow;i++) {
			line=br.readLine();
			st=new StringTokenizer(line);
			for(int j = 0;j<mapRow;j++) {
				map[i][j]=Integer.parseInt(st.nextToken());
				if(map[i][j]==1) { // 집인 경우
					homeList.add(new Point(i,j));
				}
				else if(map[i][j]==2) { // 치킨집인 경우
					chickenList.add(new Point(i,j));
				}
			}
		}
		
		answer=Integer.MAX_VALUE;
		
		dfs(0);
		
		bw.write(answer+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	public static void dfs(int currentChickenNum) {
		
		
		if(selectedChickenList.size()==maxChickenNum) {
			answer=Math.min(answer, calculateDistance());
			return;
		}
		
		if (currentChickenNum == chickenList.size()) return;
		
		// 유지하는 경우
		selectedChickenList.add(chickenList.get(currentChickenNum));
		dfs(currentChickenNum+1);
		selectedChickenList.remove(selectedChickenList.size()-1);
		
		// 폐업하는 경우
		dfs(currentChickenNum+1);
	}
	
	public static int calculateDistance() {
		// 한 집에 대해서 최소 치킨집 거리를 구하는 것이므로
		// outer for문에 homeList, inner for문에 selectedChickenList
		// 들가는 게 맞음
		
		int totalDistance=0;
		
		for(Point home:homeList) {
			int minDistance=Integer.MAX_VALUE;
			for(Point selectedChicken:selectedChickenList) {
				int distance=Math.abs(selectedChicken.x-home.x)+Math.abs(selectedChicken.y-home.y);
				minDistance=Math.min(minDistance, distance);
			}
			
			totalDistance+=minDistance;
		}
		
		return totalDistance;
	}
}
