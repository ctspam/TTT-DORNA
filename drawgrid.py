import time
import math  # <- Added for circle math
from dorna2 import Dorna

def main(robot):
    # joint orientation
    a, b, c = 82.98, -61.35, 70.80
    z_down = -7.57
    z_up = 20
    vel = 50
    accel = 70

    def move_to(x, y, z):
        robot.lmove(timeout=-1, rel=0, vel=vel, accel=accel, x=x, y=y, z=z, a=a, b=b, c=c)

    # vert 1
    move_to(245, -220, z_up)
    move_to(245, -220, z_down)
    move_to(245, -280, z_down)
    move_to(245, -280, z_up)

    # vert 2
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
    
    # --- Draw the "X" in the top-left box ---
    move_to(228, -223, z_up)       # move to top-left corner
    move_to(228, -223, z_down)     # pen down
    move_to(242, -237, z_down)     # draw diagonal
    move_to(242, -237, z_up)       # pen up

    move_to(242, -223, z_up)       # move to top-right corner
    move_to(242, -223, z_down)     # pen down
    move_to(228, -237, z_down)     # draw diagonal
    move_to(228, -237, z_up)       # pen up

    # --- Draw the "O" in the middle box ---
    center_x = 255
    center_y = -250
    radius = 8
    num_points = 24

    move_to(center_x + radius, center_y, z_up)      # move to circle start
    move_to(center_x + radius, center_y, z_down)    # pen down
    for i in range(num_points + 1):
        angle = 2 * math.pi * i / num_points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        move_to(x, y, z_down)                       # draw the circle

    move_to(center_x + radius, center_y, z_up)      # pen up at end

if __name__ == "__main__":
    robot = Dorna()
    robot.connect(host="localhost", port=443)
    main(robot)
    robot.close()
