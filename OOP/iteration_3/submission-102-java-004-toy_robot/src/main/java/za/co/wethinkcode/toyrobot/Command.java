package za.co.wethinkcode.toyrobot;


import java.util.Arrays;

public abstract class Command {
    private final String name;
    private String argument;

    public abstract boolean execute(Robot target);

    public Command(String name){
        this.name = name.trim().toLowerCase();
        this.argument = "";
    }

    public Command(String name, String argument) {
        this(name);
        this.argument = argument.trim();
    }

    public String getName() {                                                                           //<2>
        return name;
    }

    public String getArgument() {
        return this.argument;
    }

    public void setArgument(String argument) { this.argument = argument; }

    public static Command create(String instruction) {
        String[] args = instruction.toLowerCase().trim().split(" ");
//        System.out.println(Arrays.toString(args));

        switch (args[0]){
            case "shutdown":
            case "off":
                return new ShutdownCommand();
            case "help":
                return new HelpCommand();
            case "forward":
                return new ForwardCommand(args[1]);
            case "back":
                return new BackCommand(args[1]);
            case "sprint":
                return new SprintCommand(args[1]);
            case "right":
                return new RightCommand();
            case "left":
                return new LeftCommand();
            case "replay":
                if (args.length == 1){
                    return new ReplayCommand(false);
                }
                else if(args[1].contains("reversed") && args.length == 2){
                    return new ReplayCommand(true);
                }
                else if(!args[1].contains("reversed") && args.length == 2 && args[1].split("").length <= 3){
                    return new ReplayCommand(args[1], false);
                }
                else if(args[1].contains("reversed") && args.length == 3 && (args[2].split("-").length == 2 || args[2].split("-").length == 1)){
                    return new ReplayCommand(args[2], true);
                }
            case "mazerun":
                if (args.length == 1){
                    return new MazerunCommand("top");
                }
                else{
                    return new MazerunCommand(args[1]);
                }

            default:
                throw new IllegalArgumentException("Unsupported command: " + instruction);
        }
    }

    @Override
    public String toString() {
        return this.getName() + " " + this.getArgument();
    }
}

