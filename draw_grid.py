import time
from dorna2 import Dorna

# constants
PEN_DOWN_Z = 81.85
PEN_UP_Z = 91.85
VEL = 100

# Grid line function with pen up/down
def draw_line(robot, start, end):
    # moving above the start point
    robot.lmove(timeout=-1, rel=0, vel=VEL, x=start[0], y=start[1], z=PEN_UP_Z, a=start[2], b=start[3], c=start[4])
    # lowering the pen
    robot.lmove(timeout=-1, rel=0, vel=VEL, x=start[0], y=start[1], z=PEN_DOWN_Z, a=start[2], b=start[3], c=start[4])
    # drawing the line
    robot.lmove(timeout=-1, rel=0, vel=VEL, x=end[0], y=end[1], z=PEN_DOWN_Z, a=end[2], b=end[3], c=end[4])
    # raising the pen
    robot.lmove(timeout=-1, rel=0, vel=VEL, x=end[0], y=end[1], z=PEN_UP_Z, a=end[2], b=end[3], c=end[4])

# grid drawing func
def draw_grid(robot):
    print("Drawing Tic Tac Toe grid...")

    # oritentation constants
    a = 69.3
    b = -69.28
    c = 69.29

    # vert 1
    draw_line(robot,
              start=[255.56, -255.61, a, b, c],
              end=[255.56, -315.67, a, b, c])

    # vert 2
    draw_line(robot,
              start=[275.61, -255.65, a, b, c],
              end=[275.61, -315.67, a, b, c])

    # horiz 1
    draw_line(robot,
              start=[235.70, -275.62, a, b, c],
              end=[295.63, -275.62, a, b, c])

    # horiz 2
    draw_line(robot,
              start=[235.71, -295.52, a, b, c],
              end=[295.59, -295.52, a, b, c])

    print("Grid drawing complete!")

# main entry point
def main(robot):
    draw_grid(robot)

# Connect to Dorna and execute
if __name__ == "__main__":
    robot = Dorna()
    robot.connect(host="localhost", port=443)
    main(robot)
    robot.close()