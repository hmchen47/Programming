# Problem Set 6: Simulating robots
# Name: SOLUTIONS
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# For python 2.6:
from ps6_verify_movement26 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for python 2.7):
##from ps6_verify_movement27 import testRobotMovement
	  
# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)

class RobotCollection(object):
    """
    A RobotCollection represents a collection of robots in a room. It supports
    two operations:

    * You can add a robot to the collection with the add method.

    * You can iterate over the robots in the collection with
      "for robot in rc:". The iteration order is unspecified.
    """
    def __init__(self):
        """
        Initializes a RobotCollection. The collection is initially empty.
        """
        self.robots = []
        
    def add(self, robot):
        """
        Add ROBOT to the collection.

        robot: a Robot object.
        """
        self.robots.append(robot)
        
    def __iter__(self):
        """
        Return an iterator over the robots in the collection.
        """
        return iter(self.robots)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {}
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[(x, y)] = False
            
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = math.floor(pos.getX())
        y = math.floor(pos.getY())
        self.tiles[(x, y)] = True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m, n)]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return sum(self.tiles.values())
    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.random() * self.width,
                        random.random() * self.height)
    
    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return ((0 <= pos.getX() < self.width)
                and (0 <= pos.getY() < self.height))


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randrange(360)
        self.position = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.position)
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
    
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
        
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        candidatePosition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(candidatePosition):
            self.setRobotPosition(candidatePosition)
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction = random.randrange(360)

# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    visualize = False
    total_time_steps = 0.0
    for trial in range(num_trials):
        if visualize:
            anim = ps6_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        robotCollection = []
        for i in range(num_robots):
            robotCollection.append(robot_type(room, speed))
        if visualize:
            anim.update(room, robotCollection)
        while (room.getNumCleanedTiles()/float(room.getNumTiles())) < min_coverage:
            for robot in robotCollection:
                robot.updatePositionAndClean()
            total_time_steps += 1
            if visualize:
                anim.update(room, robotCollection)
        if visualize:
            anim.done()
    return total_time_steps / num_trials


# === Problem 4

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        cur_pos = self.getRobotPosition()
        cur_dir = self.getRobotDirection()
        self.setRobotDirection(random.randrange(360))
        new_pos = cur_pos.getNewPosition(cur_dir, self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)



# === Problem 5
#
# 1a) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#     showPlot1('Time to clean 80% of a 20x20 room, for various numbers of robots',
#               'Number of robots',
#               'Time / steps')
#
# 1b) How does the performance of the two robot types compare when cleaning 80%
#       of a 20x20 room?
#
#       For the given parameters, RandomWalkRobots take approximately twice as
#       long to clean the same room as StandardRobots do.
#
# 2a) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#     showPlot2('Time to clean 80% of a 300-tile room for various room shapes',
#               'Aspect Ratio',
#               'Time / steps')
#
# 2b) How does the performance of the two robot types compare when two of each
#       robot cleans 80% of rooms with dimensions 
#       10x30, 20x15, 25x12, and 50x6?
#
#       A StandardRobot takes about the same amount of time to clean rooms
#       of the same area regardless of aspect ratio.  However, it takes a
#       RandomWalkRobot an exponentially increasing amount of time to clean
#       the same amount of area as the aspect ratio of the room increases.

def showPlot1(title, x_label, y_label):
    """
    Produces a plot comparing the two robot strategies in a 20x20 room with 80%
    minimum coverage.
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


if __name__ == '__main__':
    showPlot1('Time to clean 80% of a 20x20 room, for various numbers of robots',
              'Number of robots',
              'Time/ steps')
    showPlot2('Time to clean 80% of a 400-tile room for various room shapes',
              'Aspect Ratio',
              'Time / steps')
