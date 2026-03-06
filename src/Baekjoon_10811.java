import java.util.Scanner;
public class Baekjoon_10811 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int basket=input.nextInt();
        int[] array=new int[basket];
        for(int x=0;x<array.length;x++){
            array[x]=x+1;
        }
        int count=input.nextInt();

        for(int x=0;x<count;x++){
            int i=input.nextInt()-1;
            int j=input.nextInt()-1;
            for(int y=0;y<(j-i+1)/2;y++){
                int temp=array[i+y];
                array[i+y]=array[j-y];
                array[j-y]=temp;

            }
        }
        for(int i=0;i<array.length;i++){
            System.out.print(array[i]+" ");
        }
    }
}
