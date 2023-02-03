import java.time.Clock;

//The content of this file defines a Java class named 'ThreadBot' 
//This class inherits from the predefined Java class Thread.
public class ThreadBots extends Thread {
	
	
	int Identity; //This integer variable will be the thread identifier
    char init_char;//This character will be used by each thread as the first letter in the password


	//Here we redefine the default constructor of this class.
	//By default it has no arguments, but in this example
	//We are using two arguments
	public ThreadBots(int id, char c){
		//Here we retrieve the value of the identity passed by the main class
		Identity = id;
		//Here we retrieve the value of the character passed by the main class
		init_char = c;
	}
	
	public void run(){
		
		//Clock clock = Clock.systemDefaultZone();
		//long multi_start=clock.millis();
		
		//Here is where you write the code that should crack the password
	
		// Setting password to a one character string (i,t or v)
		String password = "" + init_char;
		
		// First letter after initial char
		for (char first_char = 'a'; first_char <= 'z'; first_char ++) {
			String pw_2 = password + first_char;
			password = pw_2;
			
			// Second letter after initial char
			for (char second_char = 'a'; second_char <= 'z'; second_char++) {
				String pw_3 = password + second_char;
				password = pw_3;
				
				// Third letter after initial char
				for (char third_char = 'a'; third_char <= 'z'; third_char ++) {
					String pw_4 = password + third_char;
					password = pw_4;
					
					// Fourth letter after initial char
					for (char fourth_char = 'a'; fourth_char <= 'z'; fourth_char++) {
						
						// Checking to make sure password not already guessed
						if (ThreadAttacker.found == true) {
							return;
						}
						
						String pw_5 = password + fourth_char;
						password = pw_5;
						String my_guess = password + ThreadAttacker.challenge;
						
						// Submitting a guess for password
						int guess = my_guess.hashCode();
						
						// Guess for password is correct, output result
						if (guess == ThreadAttacker.captured) {
							// Loop is exited as ThreadAttacker set to true
							ThreadAttacker.found = true;
							
							// RECORDING TIME: amount of time it takes for a multi-threaded approach
							//long multi_end=clock.millis();
							//long total_multi_time = multi_end - multi_start;
							//System.out.print("Time for approach: " + total_multi_time + " miliseconds.\n");
							
							// displaying output results
							System.out.println("The decoded password is : " + password + "\nThe thread that cracked the code is thread # " + Identity);
							return;
							
						}
						// If guessed password incorrect go back to 4th
						password = pw_4;
					}
					// If guessed password incorrect go back to 3rd
					password = pw_3;
				}
				// If guessed password incorrect go back to 2nd
				password = pw_2;
			}
			// If guessed password incorrect go to first char
			password = "" + init_char;
			}						
}
}
