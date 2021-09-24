import java.util.Scanner; 

public class Problem15{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter column: ");
    int col = sc.nextInt();
    System.out.println("enter row");
    int row = sc.nextInt();
    for(int i=1; i<=col; i++){
      for(int j=1; j<=row; j++){
        if(j==1 || j==row || i==1 || i==col){
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
  