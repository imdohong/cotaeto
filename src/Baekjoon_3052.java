import java.util.Scanner;
import java.util.Arrays;
public class Baekjoon_3052 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int[] array=new int[10];
        int x=0;
        for(int i=0;i<10;i++){
            int num=input.nextInt();
            array[i]=num%42;
        }
        Arrays.sort(array);
        int result=1;
        for(int i=0;i<9;i++){
            if(array[i]!=array[i+1]){
                result++;
            }
        }

        System.out.println(result);
    }
}
