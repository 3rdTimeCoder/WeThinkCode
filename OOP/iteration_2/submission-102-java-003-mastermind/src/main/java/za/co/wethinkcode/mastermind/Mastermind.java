package za.co.wethinkcode.mastermind;

public class Mastermind {
    private final String code;
    private final Player player;

    public Mastermind(CodeGenerator generator, Player player){
        this.code = generator.generateCode();
        this.player = player;
    }
    public Mastermind(){
        this(new CodeGenerator(), new Player());
    }

    public static void output(String string){
        System.out.println(string);
    }

    public static int[] getCorrectDigitsAndPlaces(String code, String guess){
        int correctDigitsAndPosition = 0;
        int correctDigitsOnly = 0;
        for (int i=0; i < code.length(); i++){
            if (code.charAt(i) == guess.charAt(i)){
                correctDigitsAndPosition += 1;
            }
            else if (code.indexOf(guess.charAt(i)) != -1){
                correctDigitsOnly += 1;
            }
        }
        return new int[] { correctDigitsOnly, correctDigitsAndPosition };
    }

    public void runGame(){
//        output(code); //remove this later
        output("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.");
        int correctPosition, correctDigits;
        String guess = player.getGuess();

        while (!guess.equals("quit") && !guess.equals("exit")){
            boolean gameWon = code.equals(guess);
            int[] correctDigitsAndPlaces = getCorrectDigitsAndPlaces(code, guess);
            correctDigits = correctDigitsAndPlaces[0];
            correctPosition = correctDigitsAndPlaces[1];

            output("Number of correct digits in correct place: " + correctPosition);
            output("Number of correct digits not in correct place: " + correctDigits);
            if (!gameWon) {
                player.lostChance();
                if (!player.hasNoChances()) { output("Turns left: " + player.getChances()); }
            }

            if (gameWon){
                output("Congratulations! You are a codebreaker!");
                output("The code was: " + code);
                break;
            }

            if (player.hasNoChances()){
                output("No more turns left.");
                output("The code was: " + code);
                break;
            }

            guess = player.getGuess();
        }
    }

    public static void main(String[] args){
        Mastermind game = new Mastermind();
        game.runGame();
    }
}
