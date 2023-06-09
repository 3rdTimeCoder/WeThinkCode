package za.co.wethinkcode.mastermind;

import java.util.Arrays;
import java.util.Random;

public class CodeGenerator {
    private final Random random;

    public CodeGenerator(){
        this.random = new Random();
    }

    public CodeGenerator(Random random){
        this.random = random;
    }


    /**
     * Generates a random 4 digit code, using this.random, where each digit is in the range 1 to 8 only.
     * Duplicated digits are allowed.
     * @return the generated 4-digit code
     */
    public String generateCode(){
        String code = "";
        for (int i=0; i != 4; i++) {
            int randomNumber = this.random.nextInt(8) + 1;
            code += randomNumber;
        }
        return code;
    }
}
