package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.maze.Maze;
import za.co.wethinkcode.toyrobot.world.IWorld;
import za.co.wethinkcode.toyrobot.world.TextWorld;
import za.co.wethinkcode.toyrobot.world.TurtleWorld;

import java.util.Arrays;
import java.util.List;

public class Robot {

    private String status;
    private String name;
    private IWorld world;
    public static Position CENTRE = new Position(0,0);


    public Robot(String name) {
        this.name = name;
        this.status = "Ready";
        this.world = new TextWorld();
    }

    public Robot(String name, String world) {
        this.name = name;
        this.status = "Ready";
        if (world.equals("text")) {
            this.world = new TextWorld();
        }else{
            this.world = new TurtleWorld();
        }
    }

    public Robot(String name, String world, Maze maze) {
        this.name = name;
        this.status = "Ready";
        if (world.equals("text")) {
            this.world = new TextWorld(maze);
        }else{
            this.world = new TurtleWorld(maze);
        }
    }

    public String getStatus() {
        return this.status;
    }

    public IWorld getWorld() { return this.world; }

    public boolean handleCommand(Command command) {
        return command.execute(this);
    }

    @Override
    public String toString() {
       return "[" + world.getPosition().getX() + "," + world.getPosition().getY() + "] "
               + this.name + "> " + this.status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getName() {
        return name;
    }

    public void showObstacles() {
        world.showObstacles();
    }

    public void reset() {
        world.reset();
    }

    public Position getPosition() {
        return world.getPosition();
    }
    
     public Direction getCurrentDirection() {
         return Direction.NORTH;
     };
}