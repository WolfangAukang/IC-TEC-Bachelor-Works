import static java.lang.System.out;

public class ElevatorFitter2 {
	public static void main(String args[]){
		out.println("True or false?");
		out.println("Can you fit ten similar guys into an elevator?");
		
		int weightOfAPerson=80;
		int maximumWeight=620;
		int totalPeople=maximumWeight/weightOfAPerson;
		
		boolean confirm=totalPeople>=10;
				
		out.println(confirm);
	}

}
