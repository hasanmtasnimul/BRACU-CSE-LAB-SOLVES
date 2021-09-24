import java.util.Scanner; 

public class Problem21{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
      for(int j=1; j<=n-i; j++){ // for the space printing
        System.out.print(" "); 
      }
      for(int k=1; k<=i*2-1; k++){ //for the star printing 
        if(i==1 || i==n|| k==1|| k==i*2-1){
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
