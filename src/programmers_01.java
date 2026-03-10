public class programmers_01 {
    // 자바 프로그램의 실행 진입점 (이게 있어야 실행 버튼이 생깁니다!)
    public static void main(String[] args) {
        Solution1 sol = new Solution1();

        // 여기에 테스트하고 싶은 숫자를 넣어보세요 (예: 10, 20)
        int result = sol.solution(10, 20);

        // 결과 출력
        System.out.println("결과값은: " + result);
    }
}

// 프로그래머스에서 복사해 온 코드
class Solution1 {
    public int solution(int num1, int num2) {
        int answer = -1;
        answer = num1 + num2;
        return answer;
    }
}