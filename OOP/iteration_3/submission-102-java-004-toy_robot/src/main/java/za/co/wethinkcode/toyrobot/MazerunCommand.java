package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.maze.BasicTuple;
import za.co.wethinkcode.toyrobot.maze.MazeRunner;
import za.co.wethinkcode.toyrobot.maze.SimpleMazeRunner;
import za.co.wethinkcode.toyrobot.world.IWorld;

import java.util.ArrayList;

public class MazerunCommand extends Command{

    @Override
    public boolean execute(Robot target) {
        IWorld.Direction newDirection;
        BasicTuple currentInstruction;
        MazeRunner simpleMazeRunner = new SimpleMazeRunner();
        IWorld.Direction direction = getIWorldDirection();
        ArrayList<BasicTuple> instructions = simpleMazeRunner.mazeRun(target, direction);;

        target.setStatus("Starting maze run..");
        System.out.println(target);

        // loop through instructions and execute them.
        for (int i=0; i<instructions.size(); i++) {
            currentInstruction = instructions.get(i);

            // turn robot to face correct direction
            newDirection = getNewDirection(currentInstruction.getDirection());
            while (target.getWorld().getCurrentDirection() != newDirection) {
                Command turnRight = new RightCommand();
                turnRight.execute(target);
//                System.out.println("current dir: " + target.getWorld().getCurrentDirection() + " dir should face: " + newDirection);
            }

            // move forward
            Command goForward = new ForwardCommand(String.valueOf(currentInstruction.getSteps()));
            goForward.execute(target);
            System.out.println(target);
        }
        target.setStatus("Sorry, I cannot go outside my safe zone.");
        System.out.println(target);
        target.setStatus("I am at the " + getArgument() + " edge. (Cost: " + simpleMazeRunner.getMazeRunCost() + " steps)");

        return true;
    }

    private IWorld.Direction getNewDirection(Character direction) {
        switch (direction) {
            case 'U':
                return IWorld.Direction.UP;
            case 'D':
                return IWorld.Direction.DOWN;
            case 'L':
                return IWorld.Direction.LEFT;
            case 'R':
                return IWorld.Direction.RIGHT;
        }
        return null;
    }

    private IWorld.Direction getIWorldDirection() {
        switch (getArgument()){
            case "top":
                return IWorld.Direction.UP;
            case "bottom":
                return IWorld.Direction.DOWN;
            case "left":
                return IWorld.Direction.LEFT;
            case "right":
                return IWorld.Direction.RIGHT;
            default:
                throw new IllegalArgumentException("Unsupported direction: " + getArgument());
        }
    }

    public MazerunCommand(String argument) {
        super("mazerun", argument);
    }
}
