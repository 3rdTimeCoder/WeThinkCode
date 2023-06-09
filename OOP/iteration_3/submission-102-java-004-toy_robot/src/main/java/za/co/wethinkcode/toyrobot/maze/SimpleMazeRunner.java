package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Robot;
import za.co.wethinkcode.toyrobot.world.IWorld;

import java.util.ArrayList;

public class SimpleMazeRunner implements MazeRunner{
    private String path;
    public ArrayList<BasicTuple> mazeRun(Robot target, IWorld.Direction edgeDirection){
        String[] mazeStr = target.getWorld().getMaze();
        String edge = getStringDirection(edgeDirection);
//        String path = MazeRunnerHelper.findPath(mazeStr, edge);
        this.path = MazeRunnerHelper.findPath(mazeStr, edge);
//        if this.path.equals("U")
        ArrayList<BasicTuple> instructions = MazeRunnerHelper.createInstructions(path, edge);

        return instructions;
    }

    public int getMazeRunCost(){
        return path.length();
    }

    private String getStringDirection( IWorld.Direction direction) {
        switch (direction){
            case UP:
                return "top";
            case DOWN:
                return "bottom";
            case LEFT:
                return "left";
            case RIGHT:
                return "right";
        }
        return null;
    }
}
