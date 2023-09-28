import java.util.Scanner; 
class App{
    public static void main(String[]args){
        System.out.println("Enter your Age :-");
        Scanner sc = new Scanner(System.in);
        String x = sc.nextLine();
        int Age = Integer.parseInt(x);
        int Dif = 13 - Age;
        if (Age == 0){
            System.out.println("Invalid input");
        }else if(Age < 13){
            System.out.println("You are a child.So, you can't ride");
            System.out.println(String.format("You need to wait %d years", Dif));
        }else if(Age >= 13 && Age <= 18){
            System.out.println("You are a teenager. you can ride");
        }else if(Age <= 45){
            System.out.println("You are a adult. you can ride");
        }else if(Age <= 100){
            System.out.println("You above 45.So, you can't ride");
        }else{
            System.out.println("Invalid input");
        }
        sc.close();
        }
    }