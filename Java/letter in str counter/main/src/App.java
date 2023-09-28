import java.util.Scanner;

public class App {
    public static void main(String[] args){
       Scanner sc = new Scanner(System.in);
       String input = sc.next();
       if(input.startsWith("-"))
       {
            System.out.println("yes");
       }else{
            System.out.println("No");
       }
       sc.close();

    }
}
