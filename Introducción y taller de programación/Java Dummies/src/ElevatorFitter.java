import static java.lang.System.out;

public class ElevatorFitter {
	public static void main(String args[]){
		int weightOfAPerson;
		int elevatorWeightLimit;
		int numberOfPeople;
		
		weightOfAPerson=80;
		elevatorWeightLimit=800;
		numberOfPeople=elevatorWeightLimit/weightOfAPerson;
		
		out.println("You can put here "+numberOfPeople+" people on this elevator");
	}

}
