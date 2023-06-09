package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.world.Obstacle;

import java.util.List;

public class EmptyMaze extends AbstractMaze {
    private String[] maze;

    public EmptyMaze() {
        this.maze = new String[]{};
        System.out.println("Loaded EmptyMaze.");
    }

    @Override
    public List<Obstacle> getObstacles() {
        return setupMaze(maze);
    }

    @Override
    public String[] getMaze() { return this.maze; }
}
