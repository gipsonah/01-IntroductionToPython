"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Alex Gipson.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
allan = rg.SimpleTurtle('turtle')
allan.pen = rg.Pen('black', 16)
allan.speed = 100000000
size = 300
for k in range(22):
        allan.draw_square(size)
        allan.pen_up()
        allan.right(45)
        allan.forward(10)
        allan.left(45)
        allan.pen_down()
        size = size - 12
gavin = rg.SimpleTurtle('turtle')
gavin.pen = rg.Pen('black', 16)
gavin.speed = 10000000
size = 300
for k in range (22):
        gavin.draw_regular_polygon(3, size)
        gavin.pen_up()
        gavin.right(45)
        gavin.forward(10)
        gavin.left(45)
        gavin.pen_down()
        size = size - 12
ashlyn = rg.SimpleTurtle('turtle')
ashlyn.pen = rg.Pen('red', 8)
ashlyn.speed = 100000000
size = 300
for k in range(22):
        ashlyn.draw_square(size)
        ashlyn.pen_up()
        ashlyn.right(45)
        ashlyn.forward(10)
        ashlyn.left(45)
        ashlyn.pen_down()
        size = size - 12
patrick = rg.SimpleTurtle('turtle')
patrick.pen = rg.Pen('red', 8)
patrick.speed = 10000000
size = 300
for k in range (22):
        patrick.draw_regular_polygon(3, size)
        patrick.pen_up()
        patrick.right(45)
        patrick.forward(10)
        patrick.left(45)
        patrick.pen_down()
        size = size - 12
adam = rg.SimpleTurtle('turtle')
adam.pen = rg.Pen('black', 4)
adam.speed = 100000000
size = 300
for k in range(22):
        adam.draw_square(size)
        adam.pen_up()
        adam.right(45)
        adam.forward(10)
        adam.left(45)
        adam.pen_down()
        size = size - 12
alyssa = rg.SimpleTurtle('turtle')
alyssa.pen = rg.Pen('black', 4)
alyssa.speed = 10000000
size = 300
for k in range (22):
        alyssa.draw_regular_polygon(3, size)
        alyssa.pen_up()
        alyssa.right(45)
        alyssa.forward(10)
        alyssa.left(45)
        alyssa.pen_down()
        size = size - 12
alex = rg.SimpleTurtle('turtle')
alex.pen = rg.Pen('red', 2)
alex.speed = 10000000
size = 300
for k in range (22):
        alex.draw_square(size)
        alex.pen_up()
        alex.right(45)
        alex.forward(10)
        alex.left(45)
        alex.pen_down()
        size = size - 12
val = rg.SimpleTurtle('turtle')
val.pen = rg.Pen('red', 2)
val.speed = 10000000
size = 300
for k in range (22):
        val.draw_regular_polygon(3, size)
        val.pen_up()
        val.right(45)
        val.forward(10)
        val.left(45)
        val.pen_down()
        size = size - 12

window.close_on_mouse_click()