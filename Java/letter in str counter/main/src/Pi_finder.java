import java.util.Scanner;

public class Pi_finder {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Put your number\n>");
        int data = sc.nextInt();
        sc.close();
        System.out.println(findpi(data));
    }
    public static double findpi(int iter){
        double answer = 0;
        for(double i = 0f; i <= iter * 100; i++){
            if (i % 2 == 0){
                answer += 1 / ((i * 2) + 1);
            }
            else{
                answer -= 1 / ((i * 2) + 1); 
            }
        }
        return answer * 4;
    }

}

