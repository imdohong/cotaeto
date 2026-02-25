import java.util.Scanner;
public class Baekjoon_10813 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int basket = input.nextInt();
        int count = input.nextInt();
        int[] basket_arr=new int[basket];

        for(int i=0;i<basket_arr.length;i++){
            basket_arr[i]=i+1;
        }

        for(int x=0;x<count;x++){
            int i=input.nextInt()-1;
            int j=input.nextInt()-1;
            int temp;
            temp=basket_arr[i];
            basket_arr[i]=basket_arr[j];
            basket_arr[j]=temp;
        }

        for(int i=0;i<basket_arr.length;i++){
            System.out.print(basket_arr[i]+" ");
        }
    }
}
