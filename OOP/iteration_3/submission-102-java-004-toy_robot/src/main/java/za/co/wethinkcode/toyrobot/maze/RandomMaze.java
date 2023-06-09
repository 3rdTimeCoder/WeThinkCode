package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.world.Obstacle;

import java.util.*;

public class RandomMaze extends AbstractMaze {

    private String[] maze;

    public RandomMaze() {
//        this.maze = new Obstacle[]{new SquareObstacle(1, 1)};
        System.out.println("Loaded RandomMaze.");
        this.maze = generateRandomMaze();
    }

    @Override
    public List<Obstacle> getObstacles() {
        return setupMaze(maze);
    }

    public String[] getMaze() { return this.maze; }

    public String[] generateRandomMaze() {
        int numRows = 50;
        int numCols = 25;
        char[][] maze = new char[numRows][numCols];

        // Fill the maze with walls
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                maze[i][j] = 'x';
            }
        }

        // Define the starting and ending positions
        Random random = new Random();
        int startRow = random.nextInt(numRows / 2) * 2 + 1;
        int startCol = 0;
        int endRow = random.nextInt(numRows / 2) * 2 + 1;
        int endCol = numCols - 1;

        // Ensure there are no obstacles in the center of the maze
        int centerRow = numRows / 2;
        int centerCol = numCols / 2;
        maze[centerRow][centerCol] = ' ';
        maze[centerRow - 1][centerCol] = ' ';
        maze[centerRow + 1][centerCol] = ' ';
        maze[centerRow][centerCol - 1] = ' ';
        maze[centerRow][centerCol + 1] = ' ';

        // Carve out a path from the entrance to the exit
        carvePath(startRow, startCol, endRow, endCol, maze);

        // Remove some walls to create more paths
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (maze[i][j] == 'x' && random.nextDouble() < 0.4) {
                    maze[i][j] = ' ';
                }
            }
        }

        // Convert the maze to a String array
        String[] mazeString = new String[numRows];
        for (int i = 0; i < numRows; i++) {
            mazeString[i] = new String(maze[i]);
        }

        // Return the completed maze
//        for (char[] row : maze) {
//            System.out.println(String.valueOf(row));
//        }

//        for (String row : mazeString) {
//            System.out.println(row);
//        }
//        return mazeString;
        return mazeString;
    }

    private static void carvePath(int row, int col, int endRow, int endCol, char[][] maze) {
        List<int[]> directions = new ArrayList<>();
        directions.add(new int[]{0, 1});
        directions.add(new int[]{0, -1});
        directions.add(new int[]{1, 0});
        directions.add(new int[]{-1, 0});
        Collections.shuffle(directions);

        for (int[] d : directions) {
            // Check if the new position is valid
            int newRow = row + d[0] * 2;
            int newCol = col + d[1] * 2;
            if (newRow < 0 || newRow >= maze.length || newCol < 0 || newCol >= maze[0].length) {
                continue;
            }
            if (maze[newRow][newCol] == ' ') {
                continue;
            }

            // Carve a path to the new position
            maze[row + d[0]][col + d[1]] = ' ';
            maze[newRow][newCol] = ' ';

            // Recursively carve paths from the new position
            if (newRow != endRow || newCol != endCol) {
                carvePath(newRow, newCol, endRow, endCol, maze);
            }
        }

        // Check if the current position is the end position
        if (row == endRow && col == endCol) {
            return;
        }
    }
}
