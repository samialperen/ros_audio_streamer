#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import pyaudio
import wave

audio_name = ""

def open_audio(filename):
    try:  
        wf = wave.open(filename, 'rb')
        return wf
    except IOError:
        print("Wrong file name")
        return None
    

def callback(data):
    global audio_name
    audio_name = data.data
    return
   
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('audio_streamer', anonymous=True)

    rospy.Subscriber("audio_name", String, callback)

    
    global audio_name
    prev_name = ""
    
    
    rate = rospy.Rate(100)
    
    # Set chunk size of 1024 samples per data frame
    chunk = 1024  

    # Open the sound file
    wf = open_audio(audio_name)
    
    
    while not rospy.is_shutdown():
  
	    # Check was audio_name changed?
        if audio_name != prev_name:
            stream.close()
            p.terminate() 
	        wf = open_audio(audio_name)
	        prev_name = audio_name
        else:
            rate.sleep()
            
        if wf != None:
            if audio_name != prev_name:
	            break
	            
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

            
            

	
	# Open the video stream.
    cap = cv2.VideoCapture(video_name)
    
    while not rospy.is_shutdown():

	    
	    # Check was video_name changed?
        if video_name != prev_name:
	        cap.open(video_name)
	        prev_name = video_name
        else:
            rate.sleep()
        
        while(cap.isOpened()):
            if video_name != prev_name:
	            break        
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame',frame)
                
            else:
                print("Loop")
                cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            
    	    key = cv2.waitKey(100)    
            if key == 27 or key == 1048603:
                cv2.destroyWindow("preview")
                rospy.signal_shutdown("Program closed dude")
                exit(0)

            
	  
if __name__ == '__main__':
    listener()
