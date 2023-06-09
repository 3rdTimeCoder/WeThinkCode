package za.co.wethinkcode.mastermind;

import org.junit.jupiter.api.Test;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class CodeGeneratorTest {

    private CodeGenerator generator = new CodeGenerator();
    private String code = generator.generateCode();


    @Test
    public void codeIsFourDigits() {
        assertEquals(4, code.length());
    }

    @Test
    public void digitsInCorrectRange() {
        Character[] validNumbersArray = {'1','2','3','4','5','6','7','8'};
        List<Character> validNumbersList = Arrays.asList(validNumbersArray);
        for (int i=0; i < code.length(); i++) assertTrue(validNumbersList.contains(code.charAt(i)));
    }
}
