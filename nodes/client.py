#!/usr/bin/env python

import rospy
import dynamic_reconfigure.client

import sys

def callback(config):
    rospy.loginfo("Config set to {audio_name} ".format(**config))
    video_name = config["audio_name"]

    

if __name__ == "__main__":
    rospy.init_node("ros_audio_streamer_client")

    client = dynamic_reconfigure.client.Client("ros_audio_streamer_server", timeout=30, config_callback=callback)
    rospy.wait_for_service("/ros_audio_streamer/set_parameters")

    r = rospy.Rate(30)
    rospy.spin()







