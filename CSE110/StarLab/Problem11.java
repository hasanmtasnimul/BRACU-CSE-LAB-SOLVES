import java.util.Scanner; 

public class Problem11{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
      for(int j = 1; j<=n-i; j++){
       System.out.print(" "); 
      }
      for(int k=n-i+1; k<=n; k++){
        System.out.print(k);
      }
      System.out.println();
    }
    }
  }