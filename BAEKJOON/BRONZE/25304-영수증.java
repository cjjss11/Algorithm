import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int total = scanner.nextInt();
		int N = scanner.nextInt();
		
		int money = 0;
		
		for (int i=0; i<N; i ++) {
			int price = scanner.nextInt();
			int a = scanner.nextInt();
			money += price * a;
		}
		if (money == total) {
			System.out.print("Yes");
		}
		else {
			System.out.print("No");
		}
	}
}
