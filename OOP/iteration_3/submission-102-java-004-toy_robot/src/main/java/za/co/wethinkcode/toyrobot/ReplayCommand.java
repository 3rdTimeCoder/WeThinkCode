package za.co.wethinkcode.toyrobot;

import java.util.Collections;


public class ReplayCommand extends Command{
    private boolean reversed;
    private int arg;
    private String range;


    /*
    Default replay constructor - for when user enter replay only
    */
    public ReplayCommand(boolean reversed) {
        super("replay");
        this.reversed = reversed;
    }

    /*
    replay constructor - for when user enter replay n / replay n-m
    */
    public ReplayCommand(String argument, boolean reversed) {
        super("replay", argument);
        this.reversed = reversed;
    }

    @Override
    public boolean execute(Robot target){
        if (getArgument().isBlank() || getArgument().equals("reversed")){
            executeReplay(target, reversed);
        }
        else if (reversed && getArgument().equals("reversed")) {
            executeReplay(target, true);
        }
        else if (!getArgument().isBlank()) {
            executeReplay(target, getArgument(), reversed);
        }
        return true;
    }

    private boolean executeReplay(Robot target, boolean reversed) {

        if (reversed) {
            Collections.reverse(Play.history);
        }
        for (Command command: Play.history){
            command.execute(target);
            Play.outputStatus(target);
        }
        int commandsReplayed = Play.history.toArray().length;
        target.setStatus("replayed " +  commandsReplayed + " commands.");
        return true;
    }

    public boolean executeReplay(Robot target, String argument, boolean reversed) {
        int start, stop;
        int commandsReplayed = 0;
        int lastIndex = Play.history.size() - 1;
        String[] args = argument.split("-");

        // no history
        if (Play.history.size() == 0) {
            return true;
        }

        // is it n-m or just n?
        if (args.length == 1) {
            start = Integer.parseInt(args[0]) - 1;
            stop = 0;

            if (!reversed) {
                for (int i=start; i >= stop; i--){
                    Command command = Play.history.get(lastIndex - i);
                    executeCommand(target, command);
                    commandsReplayed++;
                }
            }else {
//                System.out.println("inside");
                for (int i=stop; i <= start; i++){
                    Command command = Play.history.get(lastIndex - i);
                    executeCommand(target, command);
                    commandsReplayed++;
                }
            }

            target.setStatus("replayed " +  commandsReplayed + " commands.");
        }
        else{
            // if 4-2
            start = Integer.parseInt(args[0]) - 1; //4
            stop = Integer.parseInt(args[1]) - 1; //2

            if (!reversed) {
                for (int i=start; i > stop; i--){
                    Command command = Play.history.get(lastIndex - i);
                    executeCommand(target, command);
                    commandsReplayed++;
                }
            }else{
                for (int i=stop+1; i <= start; i++){
                    Command command = Play.history.get(lastIndex - i);
                    executeCommand(target, command);
                    commandsReplayed++;
                }
            }

//            for (int i=start; i > stop; i--){
//                Command command = Play.history.get(lastIndex - i);
//                executeCommand(target, command);
//                commandsReplayed++;
//            }
            target.setStatus("replayed " +  commandsReplayed + " commands.");
        }
        return true;
    }

    private void executeCommand(Robot target, Command command) {
        command.execute(target);
        Play.outputStatus(target);
    }


}
