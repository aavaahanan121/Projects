import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Set<String> Users = new HashSet<String>();
        String data;

        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("'a' for add user, 'r' for remove user, 'c' check users, 'q' for quit\n>");
            data = sc.next();

            if (data.equals("a")) {
                System.out.print("User name\n>");
                data = sc.next();
                Users.add(data);
                System.out.println("Added " + data);
            } else if (data.equals("r")) {
                System.out.print("User name\n>");
                data = sc.next();
                if (Users.contains(data)) {
                    Users.remove(data);
                    System.out.println("Removed " + data);
                } else {
                    System.out.println("There is no user called " + data);
                }
            } else if (data.equals("c")) {
                System.out.println(Users);
            } else if (data.equals("q")) {
                System.out.println("bye, have a nice day.");
                break;
            }
            else{
            System.out.print(data);
            }
        }
        sc.close();

    }
}
