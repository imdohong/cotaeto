import java.util.Scanner;
public class Baekjoon_5597 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int[] array=new int[30];
        for(int i=0;i<28;i++){
            int n=input.nextInt();
            array[n-1]=1;
        }
        for(int i=0;i<30;i++){
            if(array[i]==0){
                System.out.println(i+1);
            }
        }

    }
}
