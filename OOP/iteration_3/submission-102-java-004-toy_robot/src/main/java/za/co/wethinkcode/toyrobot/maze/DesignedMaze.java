package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.world.Obstacle;

import java.util.List;

public class DesignedMaze extends AbstractMaze {
    private String[] maze;

    public DesignedMaze() {
        this.maze = getMazeAray();
        System.out.println("Loaded DesignedMaze.");
    }

    @Override
    public List<Obstacle> getObstacles() {
        return setupMaze(maze);
    }

    @Override
    public String[] getMaze() { return this.maze; }

    public String[] getMazeAray() {
        String[] maze = {
                "x xxxxxxxxxxxxxxxxxxxxxxx",
                "x         xxxxx         x",
                "x xxxxxxx xxx   xxxxxxxxx",
                "x xx      xxx x        xx",
                "x  x xxxx xxx xxxxx xx xx",
                "x xx xxxx xxx xxxxx xx xx",
                "x    x               x xx",
                "xx xxxxxx xxxxxxx xx x  x",
                "xx xxxxxx xxxxxxx xx xx x",
                "xx     xx         xx xx x",
                "xxxxxx x  xxxxxxxxxx    x",
                "xxx          xxxxxxx xxxx",
                "x x xxxx xxxxx x        x",
                "x x xxxx xxxxx x xxx xx x",
                "x x                  xx x",
                "x xx xxxxxx xxxxxxxxxxx x",
                "x    xxxxxx xxxxx xxxx  x",
                "xxxx xx     xxx   xxxx xx",
                "xxxx xx xxx xxx xxxx   xx",
                "xxxx            xxxx xxxx",
                "xxxx xx xxx xxx      xxxx",
                "xxxx xx x x xxxxxxxx    x",
                "x    xx x x          xxxx",
                "x xx xx x xxxxx xxxxxxxxx",
                "x    xx x  x    x       x",
                "x xxxxx xx x  x xxx xxx x",
                "x   xxx       x x x xxx x",
                "xxx xxxx xxx xx x x x   x",
                "xxx xxxx xxx xx x   x x x",
                "xxx x           xxxxx x x",
                "x   x xxxx xxxx          ",
                "x x x xx x xxxxxxxxxxx xx",
                "x x x    x         xxx xx",
                "x x xxxxxx xxxxxxx xxx xx",
                "xxx        xxxx    xxx xx",
                "xxxxxx xxxxx xx xxxxxx xx",
                "xxxxxx       xx    xxx xx",
                "x      xxxxx xxxxx     xx",
                "xxxxxx xx          x x xx",
                "       xx xxxxxxxxxx x xx",
                "x x xx xx        xxx x xx",
                "x x xx xxxxxxxxx     x xx",
                "x x xx           xxx x xx",
                "x x xxxxxxxxx xxxxxx x xx",
                "x      x xxxx xxx      xx",
                "x xxxxxx xxxx      xxx xx",
                "x xxxxxx      xxxx     xx",
                "x        xxxx xxxx xxx xx",
                "xxxxxxxx xxxx        x  x",
                "xxxxxxxxxxxxxxxxxxxxxxx x",
        };
        return maze;
    }

}
