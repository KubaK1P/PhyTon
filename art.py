import os
import time

art1 = """
         _
      *     *
    /   . .   \\
    |    v    |
     \\       /
       *    *
         **
"""
art2 = """
     __     __
     ()  _  ()
  [][]*     *[][]
    /   . .   \\
   ||    v    ||
  /. \\       / .\\
 /     *    *    \\
         **
        /\\/\\
"""


def art():
    if os.name == "nt":
        print(art2)
        print("""

KEVIN HAS DETECTED YOU ARE USING WINDOWS.
COMMENCING DISK FORMAT AND OS REMOVAL.


LINUX WILL BE INSTALLED IN:
        """)
        for n in range(5):
            time.sleep(1)
            print(5-n)
    else:
        print(art1)
        print("""

Kevin approves of your operating system.
Keep up the job of software development (or whatever you are doing best :3)

        """)
        time.sleep(3)
