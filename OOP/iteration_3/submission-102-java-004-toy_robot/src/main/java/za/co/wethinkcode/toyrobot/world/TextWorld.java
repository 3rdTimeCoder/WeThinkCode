package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Command;
import za.co.wethinkcode.toyrobot.Direction;
import za.co.wethinkcode.toyrobot.Play;
import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class TextWorld extends AbstractWorld{

    private List<Obstacle> obstacles;

    private String[] mazeString;

    public TextWorld(){
        super();
        this.obstacles = createObstacles();
    }

    public TextWorld(Maze maze) {
        super();
        this.obstacles = maze.getObstacles();
        this.mazeString = maze.getMaze();
    }

    public UpdateResponse updatePosition(int nrSteps) {
        int newX = this.getPosition().getX();
        int newY = this.getPosition().getY();

        if (Direction.UP.equals(this.getCurrentDirection())) {
            newY = newY + nrSteps;
        }
        else if (Direction.RIGHT.equals(this.getCurrentDirection())) {
            newX = newX + nrSteps;
        }
        else if (Direction.DOWN.equals(this.getCurrentDirection())) {
            newY = newY - nrSteps;
        }
        else if (Direction.LEFT.equals(this.getCurrentDirection()) ) {
            newX = newX - nrSteps;
        }

        Position newPosition = new Position(newX, newY);
        SquareObstacle dummyObst = new SquareObstacle(0, 0);

        if (dummyObst.blocksPath(this.getPosition(), newPosition)) {
            System.out.println("path blocked"); //not entering here. Why ???
            return UpdateResponse.FAILED_OBSTRUCTED;
        }
        else if (newPosition.isIn(this.TOP_LEFT,this.BOTTOM_RIGHT)){
            this.position = newPosition;
            return UpdateResponse.SUCCESS;
        }
            // check if path is blocked
        return UpdateResponse.FAILED_OUTSIDE_WORLD;
    };

    public void updateDirection(boolean turnRight){
        if (turnRight) {
            switch (String.valueOf(getCurrentDirection())) {
                case "UP":
                    setCurrentDirection(Direction.RIGHT);
                    break;
                case "RIGHT":
                    setCurrentDirection(Direction.DOWN);
                    break;
                case "DOWN":
                    setCurrentDirection(Direction.LEFT);
                    break;
                case "LEFT":
                    setCurrentDirection(Direction.UP);
                    break;
            }
        }
        else {
            switch (String.valueOf(getCurrentDirection())) {
                case "UP":
                    setCurrentDirection(Direction.LEFT);
                    break;
                case "RIGHT":
                    setCurrentDirection(Direction.UP);
                    break;
                case "DOWN":
                    setCurrentDirection(Direction.RIGHT);
                    break;
                case "LEFT":
                    setCurrentDirection(Direction.DOWN);
                    break;
            }
        }
    }

    @Override
    public void reset() {
        this.obstacles = new ArrayList<>();
        setCurrentDirection(Direction.UP);
        this.position = new Position(0, 0);
        Play.history = new ArrayList<>();
    }

    public List<Obstacle> createObstacles() {
        List<Obstacle> obstacles = new ArrayList<>();
        Random random = new Random();
        int randomNumber = random.nextInt(10);
        int xBound = BOTTOM_RIGHT.getX();
        int yBound = TOP_LEFT.getY();
        int randomX, randomY;

        for (int i=0; i < randomNumber; i++) {
            randomX = random.nextInt(xBound - (-xBound)) + (-xBound);
            randomY = random.nextInt(yBound - (-yBound)) + (-yBound);
            obstacles.add(new SquareObstacle(randomX, randomY));
        }
        return obstacles;
    }

    @Override
    public List<Obstacle> getObstacles() {
        return this.obstacles;
    }

    @Override
    public String[] getMaze() {
        return this.mazeString;
    }

    @Override
    public void showObstacles() {
//        List<Obstacle> obstacles = getObstacles();
        if (!obstacles.isEmpty()) {
            System.out.println("There are some obstacles:");
            for (int i=0; i < obstacles.size(); i++) {
                System.out.println(obstacles.get(i));
            }
        }
    }
}
