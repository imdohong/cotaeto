public class programmers_02 {

    // 프로그래머스 코드를 메인 클래스 안으로 가져오고, 'static'을 붙입니다.
    static class Solution {
        public int solution(int num1, int num2) {
            int answer = 0;
            answer = num1 - num2;
            return answer;
        }
    }

    // 실행을 위한 main 메서드
    public static void main(String[] args) {
        Solution s = new Solution();
        int result = s.solution(10, 5);
        System.out.println("결과값은: " + result);
    }
}