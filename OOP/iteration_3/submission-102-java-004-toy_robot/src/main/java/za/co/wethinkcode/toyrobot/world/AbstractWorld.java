package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Direction;
import za.co.wethinkcode.toyrobot.Position;

import java.util.List;

import ch.qos.logback.classic.db.SQLBuilder;

public abstract class AbstractWorld implements IWorld{

    protected final Position TOP_LEFT = new Position(-100,200);
    protected final Position BOTTOM_RIGHT = new Position(100,-200);
    protected Position position;
    protected Direction currentDirection;

    public AbstractWorld() {
        this.position = CENTRE;
        this.currentDirection = Direction.UP;
    }

    public Position getPosition() {
        return this.position;
    }

    public Direction getCurrentDirection() {
        return this.currentDirection;
    };

    public void setCurrentDirection(Direction currentDirection) {
        this.currentDirection = currentDirection;
    };

    public boolean isNewPositionAllowed(Position position) {
        Position currentPosition = getPosition();
        Obstacle dummyObst = new SquareObstacle(0, 0);
        if (dummyObst.blocksPath(currentPosition, position)){
            return false;
        }else if (!position.isIn(TOP_LEFT, BOTTOM_RIGHT)) {
            return false;
        }
        return true;
    }

    public boolean isAtEdge() {
        if (Math.abs(getPosition().getX()) == 100 || Math.abs(getPosition().getY()) == 200) {
            return true;
        }
        return false;
    }
}
