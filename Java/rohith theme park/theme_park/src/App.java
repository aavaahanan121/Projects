import java.util.Scanner; 
class App{
    public static void main(String[]args){
        System.out.println("Enter your Age :-");
        Scanner sc = new Scanner(System.in);
        String x = sc.nextLine();
        int Age = Integer.parseInt(x);
        int Dif = 13 - Age;
        if (x.startsWith("-") || Age >= 100 ){
            System.out.println("Invalid Entry !");
        }
        else{
            if (Age == 0){
                System.out.println("Invalid input");
            }
            if (Age >= 13 && Age<= 45){
                if (Age<=18){
                    System.out.println("You are a Teen. You can Ride !");
                }
                else{
                    System.out.println("You are an Adult. You can Ride");
                }
            }
            else{
                System.out.println("You Cannot Ride !");
                if (Age <= 13){
                    System.out.println("You are younger than Teen. You can ride after :-");
                    if (Dif == 1){
                        System.out.println("1 Year !");
                    }
                    else {
                        System.out.println(Dif + " Years !");
                    }
                }
                else {
                    System.out.println("You are above 45. Sorry !");
                }
                }
        }
        sc.close();
        }
    }