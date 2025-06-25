import time
from dorna2 import Dorna

def main(robot):
    # joint orientation
    a, b, c = 82.98, -61.35, 70.80
    vel = 50
    accel = 70
    def cmove_to(x, y, z, mx, my):
        robot.cmove(timeout=-1, rel=0, vel=vel, accel=accel, x=x, y=y, z=z, mx = mx, my = my, turn = 2)
    cmove_to(360, -49, 168, 362, -49)
    # x,y,z is current position (will be upper quadrant of grid)
    # midpoint determines radius
if __name__ == "__main__":
    robot = Dorna()
    robot.connect(host="localhost", port=443)
    main(robot)
    robot.close()
