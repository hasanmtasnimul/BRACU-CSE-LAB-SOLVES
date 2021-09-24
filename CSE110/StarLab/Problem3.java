import java.util.Scanner; 

public class Problem3{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter column: ");
    int col = sc.nextInt();
    System.out.println("enter row: ");
    int row = sc.nextInt();
    for(int i=1; i<=col; i++){
      for(int j=1; j<=row; j++){
        System.out.print("*"); 
      }
      System.out.println();
    }
  }
}
