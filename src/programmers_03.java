public class programmers_03 {

    static class Solution {
        public int solution(int num1, int num2) {
            int answer = 0;
            answer = num1 * num2;
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int result = s.solution(10, 5);
        System .out.println(result);
    }
}