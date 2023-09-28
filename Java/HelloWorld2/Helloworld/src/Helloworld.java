import java.util.Scanner;

public class Helloworld {
    public static void main(String[] args) {
        int Balance = 0;
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Type 'w' for Withdraw, 'd' for Deposit, 'c' for Check balance, 'quit' for exiting");
            String input = sc.next();
            if (input.equals("w")) {
                System.out.print("Enter your withdraw amount\n>");
                Balance -= sc.nextInt();
            } else if (input.equals("d")) {
                System.out.print("Enter your deposit amount\n>");
                Balance += sc.nextInt();
            } else if (input.equals("c")) {
                System.out.print("Your balance is ");
                System.out.println(Balance);
            } else if (input.equals("quit")) {
                System.out.print("Bye");
                break;
            } else {
                System.out.print("Please enter a valid input");
            }
            sc.close();
        }
    }
}