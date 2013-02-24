#!/usr/bin/env python
import tuio
from time import sleep
from utils import trace
from chalkboard import ChalkBoard

tracking = tuio.Tracking()

print "loaded profiles:", tracking.profiles.keys()
print "list functions to access tracked objects:", tracking.get_helpers()

#list of fiducials to track
track_fiducials = [0,1,2,3,4]

board = ChalkBoard()
board.loadImage("images/fab.jpg", 120, 90)

#board.loadImage("images/gear.jpg", 120, 90)
#board.loadImage("images/logo.png", 120, 90)

board.init()

try:
    while True:
        tracking.update()
        for obj in tracking.objects():
            # trace()
            if obj.id in track_fiducials:
                board.checkSpray(obj.xpos, obj.ypos, obj.id)
                # print "x: %s y:%s angle:%s" % (obj.xpos, obj.ypos, obj.angle)
                if len(track_fiducials) == 1:
                    break
                continue
        # 
        #sleep(0.100)

except KeyboardInterrupt:
    tracking.stop()