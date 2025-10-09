import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        // 잃어버리지 않은 학생 수 더하기 (기존 구조 유지)
        answer += n - lost.length;
        
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < reserve.length; i++) {
            res.add(reserve[i]);
        }
        
        List<Integer> lo = new ArrayList<>();
        for (int i = 0; i < lost.length; i++) {
            lo.add(lost[i]);
        }
        
        // --- 1. (추가된 부분) 스스로 해결하는 학생 처리 ---
        List<Integer> selfReservers = new ArrayList<>();
        for (int lostStudent : lo) {
            if (res.contains(lostStudent)) {
                selfReservers.add(lostStudent);
            }
        }
        // 스스로 해결 가능한 학생들은 lost와 reserve 목록 양쪽에서 모두 제거
        lo.removeAll(selfReservers);
        res.removeAll(selfReservers);
        // 이 학생들은 체육 수업에 참여 가능하므로 answer에 더해줌
        answer += selfReservers.size();
        

        // --- 2. (추가된 부분) 최적의 해를 찾기 위한 정렬 ---
        Collections.sort(lo);
        Collections.sort(res);
        

        // --- 기존 로직 시작 (수정 없음) ---
        List<Integer> borrowedSuccess = new ArrayList<>();

        for (int element : lo) {
            // 앞 번호 학생에게 먼저 빌리는 것이 유리하므로 순서 변경
            if (res.contains(element - 1)) {
                res.remove(Integer.valueOf(element - 1)); // 빌려준 학생은 바로 제거
                borrowedSuccess.add(element);             // 빌리기에 성공한 학생을 기록
            } else if (res.contains(element + 1)) {
                res.remove(Integer.valueOf(element + 1));
                borrowedSuccess.add(element);
            }
        }
        
        // 성공한 학생 수만큼 answer에 더하기
        answer += borrowedSuccess.size();
        
        return answer;
    }
}