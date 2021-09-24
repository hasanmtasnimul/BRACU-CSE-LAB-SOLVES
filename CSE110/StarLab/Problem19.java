import java.util.Scanner; 

public class Problem19{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
      for(int j = 1; j<=n-i; j++){
       System.out.print(" "); 
      }
      for(int k=n-i+1; k<=n; k++){
        if(i==n || k==n-i+1 || k==n){
          System.out.print(k);
        }
        else{
         System.out.print(" "); 
        }
      }
      System.out.println();
    }
    }
  }