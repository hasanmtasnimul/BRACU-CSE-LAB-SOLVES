import java.util.Scanner; 
  
public class Problem2{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
     System.out.print("*"); 
    }
  }
}