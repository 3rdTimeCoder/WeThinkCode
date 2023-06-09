package za.co.wethinkcode.toyrobot.world;

//import org.turtle.Turtle;


import java.util.Random;

public class MyProgram {
    public static void main(String[] args) {
        Random rand = new Random();
        System.out.println(rand.nextInt(6 - (-5)) + (-5));
    }

}
