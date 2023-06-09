package za.co.wethinkcode.mastermind;

import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.io.*;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.anyInt;
import static org.mockito.Mockito.when;


public class MastermindTest {

    public void simulateGame(String simulatedUserInput, String expectedLastLine){
        // Pass in mock inout
        InputStream simulatedInputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(simulatedInputStream);

        // capture output
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        // Mock Randomness
        Random randomNumberMock = Mockito.mock(Random.class);
        when(randomNumberMock.nextInt(anyInt())).thenReturn(1,  2, 3,4);
        Mastermind mastermind = new Mastermind(new CodeGenerator(randomNumberMock), new Player(simulatedInputStream));

        // call the game.
        mastermind.runGame();

        String[] linesOutput = outputStream.toString().split("\n");
        String secondLastLine = linesOutput[linesOutput.length - 2];
        assertEquals(expectedLastLine, secondLastLine);
    }

    @Test
    public void winGame(){
        String simulatedUserInput = "2435\n";
        String expectedOutput = "Congratulations! You are a codebreaker!";
        simulateGame(simulatedUserInput, expectedOutput);
    }

    @Test
    public void loseGame(){
        String simulatedUserInput = "1111\n1111\n1111\n1111\n1111\n1111\n1111\n1111\n1111\n1111\n1111\n1111\n";
        String expectedOutput = "No more turns left.";
        simulateGame(simulatedUserInput, expectedOutput);
    }
}
