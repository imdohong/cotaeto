import java.util.Scanner;
public class Baekjoon_10810 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int basket=input.nextInt();
        int[] basket_ball = new int[basket];
        int count=input.nextInt();

        for(int i=0;i<count;i++){
            int start = input.nextInt();
            int end = input.nextInt();
            int ball_num=input.nextInt();
            for(int x=start-1;x<=end-1;x++){
                basket_ball[x]=ball_num;
            }
        }
        for(int i=0;i<basket_ball.length;i++){
            System.out.print(basket_ball[i]+" ");
        }
    }
}
