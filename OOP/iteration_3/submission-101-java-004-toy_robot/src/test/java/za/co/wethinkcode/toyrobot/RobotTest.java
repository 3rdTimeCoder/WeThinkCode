package za.co.wethinkcode.toyrobot;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RobotTest {

    @Test
    void isValidCommand() {
        Robot robot = new Robot("CrashTestDummy");
        Command command = new HelpCommand();
        assertTrue(robot.handleCommand(command));
        command = new ForwardCommand("10");
        assertTrue(robot.handleCommand(command));
        command = new ShutdownCommand();
        assertTrue(robot.handleCommand(command));
    }

    @Test
    void initialPosition() {
        Robot robot = new Robot("CrashTestDummy");
        assertEquals(Robot.CENTRE, robot.getPosition());
        assertEquals("NORTH", String.valueOf(robot.getCurrentDirection()));
    }

    @Test
    public void equality() {
        assertEquals(new Position(-44, 63), new Position(-44, 63));
        assertNotEquals(new Position(-44, 63), new Position(0, 63));
        assertNotEquals(new Position(-44, 63), new Position(-44, 0));
        assertNotEquals(new Position(-44, 63), new Position(0, 0));
    }

    @Test
    void dump() {
        Robot robot = new Robot("CrashTestDummy");
        assertEquals("[0,0] CrashTestDummy> Ready", robot.toString());
    }

    @Test
    void shutdown() {
        Robot robot = new Robot("CrashTestDummy");
        Command command = new ShutdownCommand();
        assertTrue(robot.handleCommand(command));
    }

    @Test
    void forward() {
        Robot robot = new Robot("CrashTestDummy");
        Command command = new ForwardCommand("10");
        assertTrue(robot.handleCommand(command));
        Position expectedPosition = new Position(Robot.CENTRE.getX(), Robot.CENTRE.getY() + 10);
        assertEquals(expectedPosition, robot.getPosition());
        assertEquals("Moved forward by 10 steps.", robot.getStatus());
    }

    @Test
    void forwardforward() {
        Robot robot = new Robot("CrashTestDummy");
        Command command = new ForwardCommand("10");
        assertTrue(robot.handleCommand(command));
        Command command2 = new ForwardCommand("5");
        assertTrue(robot.handleCommand(command2));
        assertEquals("Moved forward by 5 steps.", robot.getStatus());
    }

    @Test
    void tooFarForward() {
        Robot robot = new Robot("CrashTestDummy");
        Command command = new ForwardCommand("1000");
        assertTrue(robot.handleCommand(command));
        assertEquals(Robot.CENTRE, robot.getPosition());
        assertEquals("Sorry, I cannot go outside my safe zone.", robot.getStatus());
    }

    @Test
    void help() {
        Robot robot = new Robot("CrashTestDummy");
        Command command = new HelpCommand();
        assertTrue(robot.handleCommand(command));
        assertEquals("I can understand these commands:\n" +
                "OFF  - Shut down robot\n" +
                "HELP - provide information about commands\n" +
                "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'", robot.getStatus());
    }

}
