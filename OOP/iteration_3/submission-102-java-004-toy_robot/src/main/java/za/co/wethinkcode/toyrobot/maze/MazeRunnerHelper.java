package za.co.wethinkcode.toyrobot.maze;

import java.util.*;

public class MazeRunnerHelper {
    // BFSA
    // Legend
    // S - starting point, E endpoint, v - visited
    private static String shortestPath = "";
    private static int obstacle_size = 8;

    public MazeRunnerHelper(){}

    public static String findPath(String[] mazeStr, String edgeDir) {
        if (mazeStr.length == 0) {
            switch (edgeDir) {
                case "top":
                    return "U";
                case "bottom":
                    return "D";
                case "left":
                    return "L";
                case "right":
                    return "R";
            }
        }

        Queue<String> paths = new LinkedList<>();
        paths.add("");
        String currentPath = "";

        char[][] maze = createMazeList(mazeStr);
        char[][] originalMaze = createMazeList(mazeStr);

        int[] end = findEdge(edgeDir, maze);
        maze[end[0]][end[1]] = 'E';

        int[] startingPoint = findCenter(maze);
        maze[startingPoint[0]][startingPoint[1]] = 'S';

        while (!findEnd(maze, currentPath, startingPoint, originalMaze)) {
            currentPath = paths.remove();

            for (char j : new char[]{'U', 'R', 'D', 'L'}) {
                String put = currentPath + j;
                int[] result = valid(maze, put, startingPoint);
//                boolean validMove = (boolean) result[0];
                boolean validMove = result[0] == 1? true : false;
                int row = result[1];
                int col = result[2];

                if (validMove && maze[row][col] != 'v') {
                    paths.add(put);
                }
            }
        }

//        visualizePath(maze, startingPoint, originalMaze, shortestPath);
        return shortestPath;

    }

    public static char[][] createMazeList(String[] mazeStr) {
//        String[] mazeRows = mazeStr.split("\n");
        if (mazeStr.length != 0) {
            char[][] maze = new char[mazeStr.length][mazeStr[0].length()];
            for (int i = 0; i < mazeStr.length; i++) {
                for (int j = 0; j < mazeStr[i].length(); j++) {
                    maze[i][j] = mazeStr[i].charAt(j);
                }
            }
            return maze;
        }
        return new char[][]{};
    }

    public static int[] findEdge(String direction, char[][] maze) {
        int[] edgeIndex = new int[2];

        if (maze.length == 0) { return null; }

        if (direction.equals("top")) {
            for (int i = 0; i < maze[0].length; i++) {
                if (maze[0][i] == ' ') {
                    edgeIndex[0] = 0;
                    edgeIndex[1] = i;
                    return edgeIndex;
                }
            }
        } else if (direction.equals("bottom")) {
            for (int i = 0; i < maze[0].length; i++) {
                if (maze[maze.length - 1][i] == ' ') {
                    edgeIndex[0] = maze.length - 1;
                    edgeIndex[1] = i;
                    return edgeIndex;
                }
            }
        } else if (direction.equals("left")) {
            for (int i = 0; i < maze.length; i++) {
                if (maze[i][0] == ' ') {
                    edgeIndex[0] = i;
                    edgeIndex[1] = 0;
                    return edgeIndex;
                }
            }
        } else if (direction.equals("right")) {
            for (int i = 0; i < maze.length; i++) {
                if (maze[i][maze[0].length - 1] == ' ') {
                    edgeIndex[0] = i;
                    edgeIndex[1] = maze[0].length - 1;
                    return edgeIndex;
                }
            }
        }

        return edgeIndex;
    }

    public static int[] findCenter(char[][] maze) {
        int row = maze.length / 2;
        int col = maze[0].length / 2;
        int[] center = {row, col};
        return center;
    }

    public static boolean findEnd(char[][] maze, String moves, int[] startingPoint, char[][] originalMaze) {
        int j = startingPoint[0];
        int i = startingPoint[1];

        for (int k = 0; k < moves.length(); k++) {
            char move = moves.charAt(k);
            if (move == 'L') {
                i--;
                if (maze[j][i] != 'S' && maze[j][i] != 'v' && maze[j][i] != 'E') {
                    maze[j][i] = 'v';
                }
            } else if (move == 'R') {
                i++;
                if (maze[j][i] != 'S' && maze[j][i] != 'v' && maze[j][i] != 'E') {
                    maze[j][i] = 'v';
                }
            } else if (move == 'U') {
                j--;
                if (maze[j][i] != 'S' && maze[j][i] != 'v' && maze[j][i] != 'E') {
                    maze[j][i] = 'v';
                }
            } else if (move == 'D') {
                j++;
                if (maze[j][i] != 'S' && maze[j][i] != 'v' && maze[j][i] != 'E') {
                    maze[j][i] = 'v';
                }
            }
        }

        if (maze[j][i] == 'E') {
            shortestPath = moves;
            return true;
        }

        return false;
    }

    public static int[] valid(char[][] maze, String moves, int[] startingPoint) {
        int j = startingPoint[0];
        int i = startingPoint[1];

        for (char move : moves.toCharArray()) {
            if (move == 'L') {
                i -= 1;
            } else if (move == 'R') {
                i += 1;
            } else if (move == 'U') {
                j -= 1;
            } else if (move == 'D') {
                j += 1;
            }

            if (!(0 <= i && i < maze[0].length && 0 <= j && j < maze.length)) {
                return new int[]{0, j, i};
            } else if (maze[j][i] == 'x') {
                return new int[]{0, j, i};
            }
        }

        return new int[]{1, j, i};
    }

    public static ArrayList<BasicTuple> createInstructions(String path, String edgeDir) {
        ArrayList<Character> pathList = new ArrayList<Character>();
        ArrayList<BasicTuple> instr = new ArrayList<BasicTuple>();

        // create path list from path string
        for (char c : path.toCharArray()) {
            pathList.add(c);
        }

        if (path.length() == 1 && (edgeDir.equals("top") || edgeDir.equals("bottom"))) {
            instr.add(new BasicTuple(pathList.get(0), 200));
            return instr;
        }else if (path.length() == 1 && (edgeDir.equals("left") || edgeDir.equals("right"))){
            instr.add(new BasicTuple(pathList.get(0), 100));
            return instr;
        }

        // create instruction list from path list.
        for (int i = 0; i < pathList.size(); i++) {
            char dir = pathList.get(i);
            instr.add(new BasicTuple(dir, obstacle_size));
        }

        return instr;
    }

    public static void visualizePath(char[][] maze, int[] startingPoint, char[][] originalMaze, String path) {
        // Displays the maze and path found on terminal
        int j = startingPoint[0];
        int i = startingPoint[1];
        StringBuilder sb = new StringBuilder();
        List<BasicTuple> pos = new ArrayList<>();

        for (char move : path.toCharArray()) {
            if (move == 'L') {
                i -= 1;
            } else if (move == 'R') {
                i += 1;
            } else if (move == 'U') {
                j -= 1;
            } else if (move == 'D') {
                j += 1;
            }
            pos.add(new BasicTuple(j, i));
        }

        for (int p=0; p < pos.size(); p++) {
            originalMaze[pos.get(p).getA()][pos.get(p).getB()] = '.';
        }

        for (char[] row : originalMaze) {
            System.out.println(row);
        }
    }
}

