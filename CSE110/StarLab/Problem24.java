import java.util.Scanner; 

public class Problem24{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    
    for(int i = 1; i<=n; i++){
      System.out.print(i);
    }
    
    for(int j=n-1; j>=1; j--){
      System.out.print(j); 
    }
    
  }
}