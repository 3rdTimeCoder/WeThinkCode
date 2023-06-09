package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class RightCommand extends Command{

    @Override
    public boolean execute(Robot target) {
        IWorld world = target.getWorld();
        world.updateDirection(true);
        target.setStatus("Turned right.");
        return true;
    }

    public RightCommand() {
        super("right");
    }
}
