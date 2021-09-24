import java.util.Scanner; 

public class Problem18{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
      for(int j=1; j<=n-i; j++){
        System.out.print(" "); 
      }
      for(int k=1; k<=i; k++){
        if(k==1 || k==i || i==n){
          System.out.print("*"); 
        }
        else{
          System.out.print(" "); 
        }
      }
      System.out.println();
    }
    
  }
}