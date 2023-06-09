package za.co.wethinkcode.toyrobot;
import za.co.wethinkcode.toyrobot.maze.*;

import java.util.ArrayList;
import java.util.Scanner;


public class Play {
    static Scanner scanner;
//    private String world = "text";
    public static ArrayList<Command> history = new ArrayList<>();

    public static void main(String[] args) {
        scanner = new Scanner(System.in);
        Robot robot;
        String world = "text";
        Maze maze = null;

        if (args.length == 1) {
            world = args[0] == "turtle"? "turtle" : "text";
        }else if (args.length == 2) {
            world = args[0] == "turtle"? "turtle" : "text";
            maze = getMaze(args[1].toLowerCase());
        }

        String name = getInput("What do you want to name your robot?");
        System.out.println("Hello Kiddo!");
        if (args.length == 0){
            robot = new Robot(name);
        }
        else if (args.length == 1) {
            robot = new Robot(name, world);
        }else{
            robot = new Robot(name, world, maze);
        }
        robot.showObstacles();

        Command command;
        boolean shouldContinue = true;
        do {
            String instruction = getInput(robot.getName() + "> What must I do next?").strip().toLowerCase();
            try {
                command = Command.create(instruction);
                shouldContinue = robot.handleCommand(command);

                if (!command.getName().equals("help") && !command.getName().equals("replay")) {
                    history.add(command);
                }

            } catch (IllegalArgumentException e) {
                robot.setStatus("Sorry, I did not understand '" + instruction + "'.");
            }
            // outputStatus(robot);
            System.out.println(robot);

        } while (shouldContinue);

        // reset robot world
        robot.getWorld().reset();
    }

    public static void outputStatus(Robot robot) { System.out.println(robot); }

    private static String getInput(String prompt) {
        System.out.println(prompt);
        String input = scanner.nextLine();

        while (input.isBlank()) {
            System.out.println(prompt);
            input = scanner.nextLine();
        }
        return input;
    }
    
    
    public static Maze getMaze(String maze) {
        switch(maze) {
            case "emptymaze":
                return new EmptyMaze();
            case "simplemaze":
                return new SimpleMaze();
            case "designedmaze":
                return new DesignedMaze();
            default:
                return new RandomMaze();
        }
    }
}
