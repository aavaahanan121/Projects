import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args){
        playGame();
    }
    
    public static void playGame(){
        System.out.println("You should guess a number between 1 and 100 --- hot = very close medium = near, close = very far");
        Random ran = new Random();
        int num = ran.nextInt(101);
        Scanner scanner = new Scanner(System.in);
        while(true){
            System.out.print("Enter your guess\n>");
            int guess = scanner.nextInt();
            if(guess == num){
                System.out.println("You win");
                break;
            }
            else if(guess > num - 5 && guess < num + 5){
                //hot
                System.out.println("Hot");
            }else if(guess > num - 15 && guess < num + 15){
                //medium
                System.out.println("Medium");
            }
            else{
                //cold
                System.out.println("Cold");
            }
        }
        scanner.close();
    }

}
