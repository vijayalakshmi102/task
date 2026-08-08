import java.util.Scanner;

class BinaryToDecimal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a binary number: ");
        int n = sc.nextInt();

        int decimal = 0;
        int power = 1;

        while (n > 0) {
            int rem = n % 10;
            decimal = decimal + rem * power;
            n = n / 10;
            power = power * 2;
        }

        System.out.println("Decimal = " + decimal);
    }
}