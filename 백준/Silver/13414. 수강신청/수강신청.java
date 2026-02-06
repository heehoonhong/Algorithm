//package ctp;

import java.io.*;
import java.util.*;

public class Main {
   
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st=new StringTokenizer(br.readLine());
		int k=Integer.parseInt(st.nextToken());
		int l=Integer.parseInt(st.nextToken());
		Map<String,Integer> map=new HashMap<>();
		Map<Integer,String> mapReverse=new HashMap<>();
		
		for(int i = 0;i<l;i++) {
			String student=br.readLine();
			// 있는지 확인
			map.put(student, i);			
		}
		//System.out.println("asdfasdf");
		for(Map.Entry<String,Integer> entry:map.entrySet()) {
			//bw.write(entry.getKey()+" "+entry.getValue()+"\n");
			mapReverse.put(entry.getValue(), entry.getKey());
		}
		
		List<Integer> reverseKey=new ArrayList<>(mapReverse.keySet());
		Collections.sort(reverseKey);
		int count=0;
		for(int key:reverseKey) {
			System.out.println(mapReverse.get(key));
			count++;
			if(count>=k) {
				break;
			}
		}
		
		// 이걸 리스트로 다시 key value 뒤집어서 만들고 key를 sort 한 다음에 그 key 대로 출력하면 될 듯
		
		
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	
}

