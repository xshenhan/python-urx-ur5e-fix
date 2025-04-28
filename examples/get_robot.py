import urx
from IPython import embed
import logging

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        #robot = urx.Robot("192.168.1.6")
        robot = urx.Robot("192.168.1.243")
        #robot = urx.Robot("localhost")
        r = robot
        print("Robot object is available as robot or r")
        r.set_tcp()
        embed()
    finally:
        robot.close()
