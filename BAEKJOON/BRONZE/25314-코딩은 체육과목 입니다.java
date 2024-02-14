import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int N = scanner.nextInt();
		int num = N / 4;
		
		for (int i=0; i<num; i++) {
			System.out.print("long ");
		}
		System.out.print("int");
	}
}
