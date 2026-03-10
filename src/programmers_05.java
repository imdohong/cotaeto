public class programmers_05 {


    static class Solution {
        public int solution(int num1, int num2) {
            int answer = 0;
//삼항연산자//
            /* int answer= (num1= num2)? 1: -1;
            return answer;*/

            if (num1== num2){
                answer= 1;
            }
            else {
                answer=-1;
            }
            return answer;

        }


        }


}
