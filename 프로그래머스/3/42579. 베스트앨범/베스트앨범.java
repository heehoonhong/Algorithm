import java.util.*;

class Solution {
    
    public static class Album{
        
        int play;
        int index;
        public Album(int play,int index){
            this.play=play;
            this.index=index;
        }
        
    }
    
    public int[] solution(String[] genres, int[] plays) {
        
        Map<String,Integer> genresMap=new HashMap<>();
        Map<String,List<Album>> albums=new HashMap<>();
        
        for(int i = 0;i<genres.length;i++){
            genresMap.put(genres[i],genresMap.getOrDefault(genres[i],0)+plays[i]);
            // 일단 이 해시맵의 value가 리스트니까 key를 먼저 넣고 
            // 그 다음에 그 key에 대한 값을 넣어야 함.
            albums.putIfAbsent(genres[i],new ArrayList<>());
            albums.get(genres[i]).add(new Album(plays[i],i));
        }
        List<Integer> result=new ArrayList<>();
        // 일단 장르에 대한 정렬이 필요하므로 장르 정렬해야 함.
        List<String> genresList=new ArrayList<>(genresMap.keySet());
        genresList.sort((g1,g2)->genresMap.get(g2)-genresMap.get(g1) );
        
        for(String genre:genresList){
            List<Album> albumList=albums.get(genre);
            albumList.sort( (a,b)-> {
                if(a.play==b.play){
                    return a.index-b.index;                    
                }
                else{
                    return b.play-a.play;
                }
            });
            // 정렬 후 result에 index 저장
            for(int i =0;i<Math.min(2,albumList.size());i++){
                result.add(albumList.get(i).index);
            }
        }
        int[] answer=new int[result.size()];
        for(int i = 0;i<result.size();i++){
            answer[i]=result.get(i);
        }
        
        return answer;
    }
}