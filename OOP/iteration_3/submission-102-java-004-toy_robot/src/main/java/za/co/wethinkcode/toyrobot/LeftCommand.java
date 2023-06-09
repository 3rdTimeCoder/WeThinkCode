package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class LeftCommand extends Command{

    @Override
    public boolean execute(Robot target) {
        IWorld world = target.getWorld();
        world.updateDirection(false);
        target.setStatus("Turned left.");
        return true;
    }

    public LeftCommand() {
        super("left");
    }
}
