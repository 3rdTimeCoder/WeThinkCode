package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import za.co.wethinkcode.toyrobot.world.SquareObstacle;

import java.util.ArrayList;
import java.util.List;

abstract class AbstractMaze implements Maze {
    protected int obstacleSize = 8;
    public AbstractMaze() {}

    public List<Obstacle> getObstacles(String[] maze) {
        return setupMaze(maze);
    }


    public boolean blocksPath(Position a, Position b) {
        return false;
    }

    public List<Obstacle> setupMaze(String[] maze) {
        int screenX, screenY;
        List<Obstacle> blocks = new ArrayList<>();

        for (int r=0; r < maze.length; r++) {
            for (int c=0; c < maze[r].length(); c++) {
                char character = maze[r].charAt(c);

                // calculate the screen x,y
                screenX = -93 + (c * obstacleSize);
                screenY = 192 - (r * obstacleSize);

                // check for 'x' representing a wall
                if (character == 'x') {
                    blocks.add(new SquareObstacle(screenX, screenY));
                }
            }
        }
        return blocks;
    }

}