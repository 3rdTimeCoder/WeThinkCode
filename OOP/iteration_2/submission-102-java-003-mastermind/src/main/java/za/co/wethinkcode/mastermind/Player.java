package za.co.wethinkcode.mastermind;

import java.io.InputStream;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Player {
    private final Scanner inputScanner;
    private int chances = 12;
    private boolean quit = false;

    public Player(){
        this.inputScanner = new Scanner(System.in);
    }

    public Player(InputStream inputStream){
        this.inputScanner = new Scanner(inputStream);
    }

    public void output(String string, boolean newline){
        if (newline) {System.out.println(string);}
        else {System.out.print(string);}
    }

     static boolean inRange(String userGuess){
        Character[] validNumbersArray = {'1','2','3','4','5','6','7','8'};
        List<Character> validNumbersList = Arrays.asList(validNumbersArray);
        for (int i=0; i < userGuess.length(); i++){
            if (!validNumbersList.contains(userGuess.charAt(i))){return false;}
        }
        return true;
    }

    /**
     * Gets a guess from user via text console.
     * This must prompt the user to re-enter a guess until a valid 4-digit string is entered, or until the user enters `exit` or `quit`.
     *
     * @return the value entered by the user
     */
    public String getGuess(){
        String userGuess = null;
        while (true){
            output("Input 4 digit code:", true);
            userGuess = this.inputScanner.nextLine().toLowerCase();

            if (userGuess.equals( "quit") || userGuess.equals("exit")){
                output("We are sorry to see you go, Goodbye!.", true);
                break;
            }
            if (userGuess.length() == 4 && inRange(userGuess)){break;}
            output("Please enter exactly 4 digits (each from 1 to 8).", true);
        }
        return userGuess;
    }

    public int getChances(){
        return this.chances;
    }

    public void lostChance(){
        if (!this.hasNoChances()) {this.chances--;}
    }

    public boolean hasNoChances(){
        return this.getChances() == 0;
    }

    public boolean wantsToQuit(){
        return this.quit;
    }

}
