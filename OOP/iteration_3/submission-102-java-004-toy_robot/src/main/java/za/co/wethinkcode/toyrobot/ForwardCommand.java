package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class ForwardCommand extends Command {
    @Override
    public boolean execute(Robot target) {
        IWorld world = target.getWorld();
        int nrSteps = Integer.parseInt(getArgument());
        if (world.updatePosition(nrSteps) == IWorld.UpdateResponse.SUCCESS) {
            target.setStatus("Moved forward by "+nrSteps+" steps.");
        }
        else if (world.updatePosition(nrSteps) == IWorld.UpdateResponse.FAILED_OBSTRUCTED) {
            target.setStatus("Sorry, there is an obstacle in the way.");
        }
        else {
            target.setStatus("Sorry, I cannot go outside my safe zone.");
        }
        return true;
    }

    public ForwardCommand(String argument) {
        super("forward", argument);
    }
}

