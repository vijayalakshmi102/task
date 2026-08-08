import java.util.Scanner;

class DecimalToBinary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a decimal number: ");
        int n = sc.nextInt();

        int binary = 0;
        int place = 1;

        while (n > 0) {
            int rem = n % 2;
            binary = binary + rem * place;
            n = n / 2;
            place = place * 10;
        }

        System.out.println("Binary = " + binary);
    }
}