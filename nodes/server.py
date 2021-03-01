#!/usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from ros_audio_streamer.cfg import QTConfig

def callback(config, level):
    rospy.loginfo("""Reconfigure Request: {audio_name} """.format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("ros_audio_streamer_server", anonymous = False)

    srv = Server(QTConfig, callback)
    rospy.spin()
