import java.util.*;

class Solution {
    
    public static class Album implements Comparable<Album>{
        
        int index, playCount;
        public Album(int index,int playCount){
            this.index=index;
            this.playCount=playCount;
        }
        
        @Override
        public int compareTo(Album otherAlbum){
            if(otherAlbum.playCount==this.playCount){
                return this.index-otherAlbum.index;
            }
            else{
                return otherAlbum.playCount-this.playCount;
            }
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        int len=genres.length;
        Map<String,Integer> genreRank=new HashMap<>();
        Map<String,List<Album>> albumRank=new HashMap<>();
        
        // 데이터 초기화
        for(int i=0;i<len;i++){
            genreRank.put(genres[i],genreRank.getOrDefault(genres[i],0)+plays[i]);
            albumRank.putIfAbsent(genres[i],new ArrayList<>());
            albumRank.get(genres[i]).add(new Album(i,plays[i]));
        }
        
        // 장르의 플레이 수를 기준으로 정렬
        List<String> sortedGenres=new ArrayList<>(genreRank.keySet());
        sortedGenres.sort((a,b)->genreRank.get(b)-genreRank.get(a));
        
        List<Integer> ans = new ArrayList<>();
        
        for(String genre:sortedGenres){
            List<Album> albumList=albumRank.get(genre);
            Collections.sort(albumList);
            for(int i=0;i<Math.min(2,albumList.size());i++){
                ans.add(albumList.get(i).index);
            }
        }
        
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}