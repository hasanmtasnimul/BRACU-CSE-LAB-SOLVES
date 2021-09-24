import java.util.Scanner; 

public class Problem17{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    
    for(int i = 1; i<=n; i++){
      for(int j=1; j<=i; j++){
        if(j==i || j==1 || i==n){
         System.out.print(j); 
        }
        else{
         System.out.print(" "); 
        }
      }
      System.out.println();
    }
    
  }
}