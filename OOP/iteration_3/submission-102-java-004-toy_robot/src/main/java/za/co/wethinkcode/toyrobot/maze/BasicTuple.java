package za.co.wethinkcode.toyrobot.maze;

import java.util.Objects;

public class BasicTuple {
    private int a;
    private final int b;

    private Character direction;

    public BasicTuple(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public BasicTuple(char direction, int b) {
        this.direction = direction;
        this.b = b;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public int getSteps() {
        return b;
    }

    public Character getDirection() {
        return direction;
    }

    @Override
    public String toString() {
        return "(" + Objects.requireNonNullElseGet(direction, () -> this.a) + "," + this.b + ")";
    }
}
