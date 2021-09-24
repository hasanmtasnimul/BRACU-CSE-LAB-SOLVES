import java.util.Scanner; 

public class Problem7{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter number: ");
    int n = sc.nextInt();
    for(int i=1; i<=n; i++){
      for(int j=1; j<=n-i; j++){ //loop for the space
       System.out.print(" ");   
      }
      for(int k=1; k<=i; k++){ // loop for printing the stars
        System.out.print("*"); 
      }
      System.out.println();
    }
    }
    
  }
