#!/usr/bin/env python

import rospy
import dynamic_reconfigure.client

import pyaudio
import wave

def callback(config):
    rospy.loginfo("Config set to {audio_name} ".format(**config))
    filename = config["audio_name"]
    
    # Set chunk size of 1024 samples per data frame
    chunk = 1024  

    # Open the sound file 
    wf = wave.open(filename, 'rb')

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)

    # Read data in chunks
    data = wf.readframes(chunk)

    # Play the sound by writing the audio data to the stream
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    # Close and terminate the stream
    stream.close()
    p.terminate()

    

if __name__ == "__main__":
    rospy.init_node("ros_audio_streamer_client")

    client = dynamic_reconfigure.client.Client("ros_audio_streamer_server", timeout=30, config_callback=callback)
    rospy.wait_for_service("/ros_audio_streamer/set_parameters")

    r = rospy.Rate(30)
    rospy.spin()







