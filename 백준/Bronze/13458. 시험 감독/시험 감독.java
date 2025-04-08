//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		int numTestRoom=Integer.parseInt(br.readLine());
		int[] testRooms=new int[numTestRoom];
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		for(int i = 0;i<numTestRoom;i++) {
			testRooms[i]=Integer.parseInt(st.nextToken());
		}
		
		String l=br.readLine();
		st=new StringTokenizer(l);
		int numMain=Integer.parseInt(st.nextToken());
		int numSub=Integer.parseInt(st.nextToken());
		
		
		long cntMain=0;
		long cntSub=0;
		
		// 총감독관이 감독하는 학생 수 빼기
		for(int i = 0;i<numTestRoom;i++) {
			if(testRooms[i]<=numMain) {
				cntMain++;
				testRooms[i]=0;
			}
			else {
				cntMain++;
				testRooms[i]=testRooms[i]-numMain;
				
			}
		}
		
		
		// 부감독관이 감독하는 학생 수 빼기
		for(int i = 0;i<numTestRoom;i++) {
			if(testRooms[i] > 0) {
		        cntSub += (testRooms[i] + numSub - 1) / numSub;
		    }
		}
		
		
		bw.write(cntMain+cntSub+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
