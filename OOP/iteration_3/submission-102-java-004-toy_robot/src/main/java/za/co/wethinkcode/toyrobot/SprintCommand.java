package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class SprintCommand extends Command{

    public SprintCommand(String argument) { super("sprint", argument); }

    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());
//        System.out.println(Play.history.get(Play.history.size() - 1).getName());

        for (int steps=nrSteps; steps>0; steps--){
            ForwardCommand command = new ForwardCommand(String.valueOf(steps));
            command.execute(target);
            if (steps != 1){
                Play.outputStatus(target);
            }
        }
        return true;
    }

//    public boolean execute(Robot target) {
//        int nrSteps = Integer.parseInt(getArgument());
//        execute(target, nrSteps);
//        return true;
//    }
//
//    public boolean execute(Robot target, int steps) {
//        if (steps == 0) { return true; }
//        ForwardCommand command = new ForwardCommand(String.valueOf(steps));
//        command.execute(target);
//        return execute(target, steps - 1);
//    }
}
