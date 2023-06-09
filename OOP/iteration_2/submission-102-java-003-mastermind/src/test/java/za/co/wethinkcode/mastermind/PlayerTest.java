package za.co.wethinkcode.mastermind;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

public class PlayerTest {

    public void simulateGame(String simulatedUserInput, String expectedLine, Player player){
        // Pass in mock inout
        InputStream simulatedInputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(simulatedInputStream);

        // capture output
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        // call the game.
        player.getGuess();

        String[] linesOutput = outputStream.toString().split("\n");
        assertTrue(Arrays.asList(linesOutput).contains(expectedLine));
    }

    @Test
    public void moreThan4Digits(){
        String inputStreamData = "12345\nquit\n";
        InputStream inputStream = new ByteArrayInputStream(inputStreamData.getBytes());

        Player player = new Player(inputStream);
//        System.out.println(Arrays.toString(test(inputStreamData , "Please enter exactly 4 digits (each from 1 to 8).", player)));
        simulateGame(inputStreamData , "Please enter exactly 4 digits (each from 1 to 8).", player);
    }

    @Test
    public void notDigits(){
        String inputStreamData = "abcd\nexit\n";
        InputStream inputStream = new ByteArrayInputStream(inputStreamData.getBytes());

        Player player = new Player(inputStream);
        simulateGame(inputStreamData , "Please enter exactly 4 digits (each from 1 to 8).", player);
    }

    @Test
    public void notValidRangeZero(){
        String inputStreamData = "1230\nquit\n";
        InputStream inputStream = new ByteArrayInputStream(inputStreamData.getBytes());

        Player player = new Player(inputStream);
        simulateGame(inputStreamData , "Please enter exactly 4 digits (each from 1 to 8).", player);
    }
    @Test
    public void notValidRangeNine(){
        String inputStreamData = "1294\n1234\n";
        InputStream inputStream = new ByteArrayInputStream(inputStreamData.getBytes());

        Player player = new Player(inputStream);
        simulateGame(inputStreamData , "Please enter exactly 4 digits (each from 1 to 8).", player);
    }
    @Test
    public void quitGame(){
        String inputStreamData = "quit";
        InputStream inputStream = new ByteArrayInputStream(inputStreamData.getBytes());

        Player player = new Player(inputStream);
        simulateGame(inputStreamData , "We are sorry to see you go, Goodbye!.", player);
    }
    @Test
    public void exitGame(){
        String inputStreamData = "exit";
        InputStream inputStream = new ByteArrayInputStream(inputStreamData.getBytes());

        Player player = new Player(inputStream);
        simulateGame(inputStreamData , "We are sorry to see you go, Goodbye!.", player);
    }

    @Test
    public void shouldStartWith12Chances() {
        Player player = new Player();
        assertEquals(12, player.getChances());
    }

    @Test
    public void canLoseAChance() {
        Player player = new Player();
        int chances = player.getChances();
        player.lostChance();
        assertEquals(chances - 1, player.getChances());
    }

    @Test
    public void noMoreChances() {
        Player player = new Player();
        int chances = player.getChances();
        for (int i=0; i<chances; i++) {
            assertFalse(player.hasNoChances());
            player.lostChance();
        }
        assertTrue(player.hasNoChances());
    }

    @Test
    public void cannotLoseChanceIfNoneAvailable() {
        Player player = new Player();
        int chances = player.getChances();
        for (int i = 0; i < chances + 1; i++) {
            player.lostChance();
        }
        assertEquals(0, player.getChances());
    }

}
