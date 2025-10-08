import java.util.HashSet;

class Solution {
    // 1. 중복된 숫자가 생성될 수 있으므로 Set을 사용하여 유니크한 값만 저장합니다.
    private HashSet<Integer> numberSet = new HashSet<>();

    public int solution(String numbers) {
        char[] digits = numbers.toCharArray();
        boolean[] visited = new boolean[digits.length];

        // 2. DFS를 통해 가능한 모든 숫자 조합을 찾습니다.
        // ""는 숫자 조합을 시작하기 위한 초기값입니다.
        dfs("", digits, visited);

        int count = 0;
        // 3. Set에 저장된 모든 숫자를 하나씩 꺼내 소수인지 판별합니다.
        for (int num : numberSet) {
            if (isPrime(num)) {
                count++;
            }
        }
        return count;
    }

    /**
     * DFS (깊이 우선 탐색)를 사용하여 숫자 조합을 만듭니다.
     * @param current 현재까지 만들어진 숫자 문자열
     * @param digits 원본 숫자 배열
     * @param visited 각 숫자의 사용 여부를 추적하는 배열
     */
    private void dfs(String current, char[] digits, boolean[] visited) {
        // 4. 사용하지 않은 숫자를 찾아 현재 숫자의 뒤에 붙입니다.
        for (int i = 0; i < digits.length; i++) {
            if (!visited[i]) {
                visited[i] = true; // 현재 숫자를 사용했다고 표시
                String newNumber = current + digits[i];
                numberSet.add(Integer.parseInt(newNumber)); // 새로 만든 숫자를 Set에 추가
                
                // 재귀 호출을 통해 다음 자리 숫자를 찾습니다.
                dfs(newNumber, digits, visited); 
                
                // 5. 중요: 재귀 호출이 끝나면, 다음 조합을 위해 현재 숫자를 "사용 안 함" 상태로 되돌립니다. (백트래킹)
                visited[i] = false; 
            }
        }
    }

    /**
     * 소수인지 판별하는 메서드 (에라토스테네스의 체 원리 일부 적용)
     */
    private boolean isPrime(int n) {
        // 0과 1은 소수가 아닙니다.
        if (n < 2) {
            return false;
        }
        // 2부터 n의 제곱근까지만 나누어 확인하면 됩니다.
        // 약수는 대칭적으로 존재하기 때문입니다. (예: 12의 약수는 1, 2, 3, 4, 6, 12. sqrt(12)≈3.46. 3까지만 확인해도 됨)
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false; // 나누어 떨어지면 소수가 아님
            }
        }
        return true; // 나누어 떨어지지 않으면 소수
    }
}