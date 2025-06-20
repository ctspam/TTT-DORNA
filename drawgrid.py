import time
from dorna2 import Dorna

def main(robot):
    # joint orientation
    a, b, c = 82.98, -61.35, 70.80
    z_down = -7.57
    z_up = 20
    vel = 30
    accel = 50

    def move_to(x, y, z):
        robot.lmove(timeout=-1, rel=0, vel=vel, accel=accel, x=x, y=y, z=z, a=a, b=b, c=c)

    # vert 1
    move_to(245, -220, z_up)
    move_to(245, -220, z_down)
    move_to(245, -280, z_down)
    move_to(245, -280, z_up)

    #vert 2
    move_to(265, -220, z_up)
    move_to(265, -220, z_down)
    move_to(265, -280, z_down)
    move_to(265, -280, z_up)

    # horiz 1
    move_to(225, -240, z_up)
    move_to(225, -240, z_down)
    move_to(285, -240, z_down)
    move_to(285, -240, z_up)

    # horiz 2
    move_to(225, -260, z_up)
    move_to(225, -260, z_down)
    move_to(285, -260, z_down)
    move_to(285, -260, z_up)

if __name__ == "__main__":
    robot = Dorna()
    robot.connect(host="localhost", port=443)
    main(robot)
    robot.close()
