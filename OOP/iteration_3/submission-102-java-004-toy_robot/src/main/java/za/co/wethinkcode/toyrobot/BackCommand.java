package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class BackCommand extends Command{

    @Override
    public boolean execute(Robot target) {
        IWorld world = target.getWorld();
        int nrSteps = Integer.parseInt(getArgument());
        if (world.updatePosition(-nrSteps) == IWorld.UpdateResponse.SUCCESS){
            target.setStatus("Moved back by "+nrSteps+" steps.");
        } else {
            target.setStatus("Sorry, I cannot go outside my safe zone.");
        }
        return true;
    }

    public BackCommand(String argument) {
        super("back", argument);
    }
}
