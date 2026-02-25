import java.util.Scanner;
public class Baekjoon_2562 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int[] arr = new int[9];
        int max=0;
        int num=0;
        for(int i=0;i<arr.length;i++){
            arr[i]=input.nextInt();

            if(max<arr[i]){
                max = arr[i];
                num = i+1;
            }
        }
        System.out.println(max);
        System.out.println(num);
    }
}
