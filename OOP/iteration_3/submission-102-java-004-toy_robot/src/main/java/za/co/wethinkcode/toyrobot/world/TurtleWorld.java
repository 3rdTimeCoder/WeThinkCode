package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Command;
import za.co.wethinkcode.toyrobot.Play;
import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;

import java.util.List;

public class TurtleWorld extends AbstractWorld{

    private Turtle robot;
    private TextWorld textWorld;

    private int obstacleSize;

    private double angle = 90.0;

    public TurtleWorld(){
        super();
        this.robot = new Turtle();
        this.textWorld = new TextWorld();
        this.obstacleSize = 5;
    }

    public TurtleWorld(Maze maze){
        super();
        this.robot = new Turtle();
        this.textWorld = new TextWorld(maze);
        this.obstacleSize = 8;
    }

    public void setupTurtle(Turtle robot) {
        robot.setPosition(0.0, 0.0, 90.0);
        robot.shapeSize(15,15);
        robot.bgcolor("black");
        robot.width(0.8);
    }

    public void displayBox() {
        setupTurtle(this.robot);
        this.robot.penColor("white");
        this.robot.up();
        this.robot.setPosition(this.TOP_LEFT.getX(), this.TOP_LEFT.getY());
        this.robot.setDirection(0.0);
        this.robot.down();
        this.robot.forward(this.BOTTOM_RIGHT.getX() * 2);
        this.robot.setDirection(270.0);
        this.robot.forward(this.TOP_LEFT.getY() * 2);
        this.robot.setDirection(180.0);
        this.robot.forward(this.BOTTOM_RIGHT.getX() * 2);
        this.robot.setDirection(90.0);
        this.robot.forward(this.TOP_LEFT.getY() * 2);
        this.robot.up();
        this.robot.setPosition(0.0, 0.0, 90.0);
        this.robot.down();
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
            if (nrSteps >= 0){
                this.robot.forward(nrSteps);
            }
            else{
                this.robot.backward(nrSteps);
            }
            this.position = newPosition;
            return UpdateResponse.SUCCESS;
        }

        // check if path is blocked
        return UpdateResponse.FAILED_OUTSIDE_WORLD;
    };

    public void updateDirection(boolean turnRight){
        if (turnRight) {
            this.robot.right(this.angle);
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
            this.robot.left(this.angle);
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
        textWorld.reset();
        robot.up();
        robot.setDirection(0.0);
        robot.setPosition(0,0);
        robot.down();
    }

    @Override
    public List<Obstacle> getObstacles() {
        return textWorld.getObstacles();
    }

    @Override
    public String[] getMaze() {
        return textWorld.getMaze();
    }

    @Override
    public void showObstacles() {
        List<Obstacle> obstacles = textWorld.getObstacles();
        displayBox();
        for (int i=0; i < obstacles.size(); i++) {
            drawObstacle(obstacles.get(i));
        }
        this.robot.setPosition(0.0, 0.0, 90.0);
        this.robot.show();
        this.robot.penColor("red");
        this.robot.down();
    }

    public void drawObstacle(Obstacle obstacle) {
        this.robot.up();
        this.robot.hide();
        this.robot.setPosition(obstacle.getBottomLeftX(), obstacle.getBottomLeftY());
        this.robot.penColor("white");
        this.robot.down();
        this.robot.setDirection(this.angle);
        drawRectangle();
        this.robot.up();
    }

    public void drawRectangle() {
        this.robot.forward(this.obstacleSize);
        this.robot.left(this.angle);
        this.robot.forward(this.obstacleSize);
        this.robot.left(this.angle);
        this.robot.forward(this.obstacleSize);
        this.robot.left(this.angle);
        this.robot.forward(this.obstacleSize);
    }
}
