package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import za.co.wethinkcode.toyrobot.world.SquareObstacle;

import java.util.ArrayList;
import java.util.List;

public class SimpleMaze extends AbstractMaze {

    private List<Obstacle> maze = new ArrayList<>();

    public SimpleMaze() {
        // Obstacle obst = new SquareObstacle(1, 1);
        maze.add(new SquareObstacle(1, 1));
        System.out.println("Loaded SimpleMaze.");
    }

    @Override
    public List<Obstacle> getObstacles() {
        // Obstacle obst = new SquareObstacle(1, 1);
        return this.maze;
    }

    @Override
    public String[] getMaze() { return new String[50]; }

}
