import java.util.Scanner; 

public class Problem23{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    for(int i = 1; i<=n; i++){
      for(int j=1; j<=n-i; j++){
        System.out.print(" ");
      }
      for(int k=1; k<=2*i-1; k++){
        if(k==1 || k==2*i-1){
         System.out.print(k); 
        }
        else{
         System.out.print(" "); 
        }
      }
      System.out.println();
    }
    
    //second loop
    for(int l=n-1; l>=1; l--){
      for(int m = n-l; m>=1; m--){
       System.out.print(" "); 
      }
      for(int o=1; o<=2*l-1; o++){
        if(o==1 || o==2*l-1){
         System.out.print(o); 
        }
        else{
         System.out.print(" "); 
        }
      }
      System.out.println();
    }
    }
    
  }
