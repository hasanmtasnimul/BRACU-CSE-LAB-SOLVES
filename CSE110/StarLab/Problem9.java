import java.util.Scanner; 

public class Problem9{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
      for(int j=1; j<=n-i; j++){ // for the space printing
        System.out.print(" "); 
      }
      for(int k=1; k<=i*2-1; k++){ //for the star printing 
        System.out.print("*"); 
      }
      
      System.out.println();
    }
  }
}
