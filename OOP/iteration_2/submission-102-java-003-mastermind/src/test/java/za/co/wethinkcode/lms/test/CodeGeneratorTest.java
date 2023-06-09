package za.co.wethinkcode.lms.test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import za.co.wethinkcode.mastermind.CodeGenerator;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.anyInt;
import static org.mockito.Mockito.when;


class CodeGeneratorTest {

    @BeforeEach
    void setUp() {
    }

    @Test
    void testGenerateCode() {
        Random randomNumberMock = Mockito.mock(Random.class);
        when(randomNumberMock.nextInt(anyInt()))
                .thenReturn(0, 1, 2, 3);
        when(randomNumberMock.nextInt())
                .thenReturn(0, 1, 2, 3);
//        when(randomNumberMock.ints(anyInt(),anyInt(),anyInt()))
//                .thenReturn(IntStream.of(1,2,3,4));

        CodeGenerator generator = new CodeGenerator(randomNumberMock);

        assertEquals("1234", generator.generateCode());
    }

    @Test
    void testValidCode() {
        CodeGenerator generator = new CodeGenerator();
        char oneChar = Integer.toString(1).charAt(0);
        char eightChar = Integer.toString(8).charAt(0);
        for(int i = 0; i < 100; i++){
            String code = generator.generateCode();
            code.chars().forEach(digit -> {
                assertTrue(digit >= oneChar && digit <= eightChar);
            });
        }
    }
}