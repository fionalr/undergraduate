//The content of this file defines a Java main class named 'ThreadAttacker' 
//This class contains the main method from where the whole program (project) 
//starts its execution


// In order to perform timed experiments, java clock is later used though 
// some indicated lines of code must be uncommented. 
import java.time.Clock;

public class ThreadAttacker {
	//This is the challenge value, you can modify the value if you want
	public static String challenge = "challenge_sequence";
	//This is the password. It is here to help us compute the correct response that corresponds to the challenge
	public static String password = "virus"; 
	//This is the variable that represents the captured response
	public static int captured;
	//This is the variable that will be used by the thread to inform each other that the password has been cracked
	//For instance, if a thread cracks the password, it update the value of this variable to true
	public static boolean found = false;
	

	//The main method, here starts the execution	
	public static void main(String[] args) throws InterruptedException 
	{
		//tempx is a temporary string variable that we are using to create the concatenation of the password with the challenge 
		String tempx = password + challenge;
		//Here we create the response by computing the hash of the previously computed string object
		captured = tempx.hashCode();
		
		
		//Thread creation and instanciation (three threads are created)
		ThreadBots t_1 = new ThreadBots(1,'i');
		ThreadBots t_2 = new ThreadBots(2, 'v');
		ThreadBots t_3 = new ThreadBots(3, 't');
		
		// RECORDING : amount of time for a single thread. Make sure to uncomment the .join()
		//Clock clock = Clock.systemDefaultZone();
		//long single_start=clock.millis();
		
		t_1.start();
		//t_1.join();
		t_2.start();
		//t_2.join();
		t_3.start();
		//t_3.join();
		
		//long single_end=clock.millis();
		//long total_multi_time = single_end - single_start;
		//System.out.print("Time for  approach: " + total_multi_time + " miliseconds.\n");
		

	
		

	}
	
}