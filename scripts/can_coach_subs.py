#!/usr/bin/env python
import sys
sys.path.append('~/anaconda3/lib/python3.7/site-packages/panda/')
#from panda import Panda
import binascii
#import bitstring
import time
import datetime
#import serial
import csv
#import cantools
#import pandas as pd
import numpy as np
#import simpleaudio as sa
#import matplotlib.pyplot as plt
import liveRadar as lt
import kalmanTracking as kt
#import osascript
#import keyboard
import random
import threading

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Float64
from visualization_msgs.msg import Marker
from geometry_msgs.msg import TwistStamped

from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine, Sawtooth, WhiteNoise, Pulse, Square
import threading, time, random


startTime = time.time() #reference start time
validTime = time.time()
counter = 0
# osascript.osascript("set volume output volume " + volume)

low = Sine(300)
high = Sine(600)
slow = low.to_audio_segment(duration=200)
fast = high.to_audio_segment(duration=200)

play(slow)
play(fast)

df = 0.04
leader = kt.KF_Object([5,0],0, 0, df, 1,1,1)
reportTime = time.time()


centerHz = 500
widthHz = 100
d = 0.25 #duration of beeps
vmax = 100 #maximum volume
#slower = sound(centerHz-widthHz,d,vmax)
#slow = sound(centerHz-widthHz,d,50)
#fast = sound((centerHz+widthHz),d,50)
#faster = sound((centerHz+widthHz),d,vmax)
lastBeep = time.time()
start = time.time()

def printit():
	t = threading.Timer(0.5, printit)
	t.start()
	# print(time.time())
    # print('anything')
	print(th)
	if th > 2.1:
		rospy.loginfo("faster")
		play(fast)
		#if th > 2.2:
		#play_obj = sa.play_buffer(faster,1,2,44100) #two higher beeps indicating speed up
	if th < 2.1 and th > 2.05:
		rospy.loginfo("fast")
		play(fast)
		#play_obj = sa.play_buffer(fast,1,2,44100)
	if th < 1.9 and th != -1:
		# if th < 1.8:
		play(slow)
		rospy.loginfo("slower")
        #play_obj = sa.play_buffer(slower,1,2,44100)
	if th > 1.9 and th < 1.95:
		play(slow)
        #play_obj = sa.play_buffer(slow,1,2,44100)
		rospy.loginfo("slow")

	def cancel():
		t.cancel()

def sound():
	print(time.ctime())
	if th > 2.05:
		play(slow)
	if th < 1.95:
		play(fast)
	if th == -1:
		pass
	threading.Timer(interval,sound).start()

interval = .5

	

#ticker = threading.Event()


gnewLeadMeasurement = 1
gmyDetections = []#np.empty_like([[0,0]])
gnewVel=0.0


def callback869(data):
    # print("lead")
    global gnewLeadMeasurement
    gnewLeadMeasurement = data.point.x

def callbackvel(data):
    # print("speed")
    global gnewVel 
    gnewVel= data.twist.linear.x
    # print('speed ', data.twist.linear.x )

def callback384(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    #np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0) 
    # print ("trackA0")
    # print(data.pose.position.x, data.pose.position.y)
def callback385(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0) 
def callback386(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0) 
def callback387(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback388(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback389(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback390(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback391(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback392(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback393(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback394(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback395(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback396(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback397(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback398(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)
def callback399(data):
    global gmyDetections
    gmyDetections.append([data.pose.position.x, data.pose.position.y])
    # np.append(gmyDetections,[[data.pose.position.x, data.pose.position.y]],axis=0)

leadDist = 20
lead869 = 0
velocity = 40
vArray = []
aArray = []
leadArray = []
thArray = []
relvArray = []
thTime = []
twos = []
th = 3.14159
myrelv = 3
relv = -50
accel = -50
leadPosition=[3,0]
lead = 0




try:
	rospy.init_node('can_coach_subs', anonymous=True)
	rospy.Subscriber("/vehicle/vel", TwistStamped,callbackvel)
	print('subscribing')
	rospy.Subscriber("/vehicle/distanceEstimator/dist", PointStamped, callback869)
	rospy.Subscriber("/track_a0", Marker, callback384)
	rospy.Subscriber("/track_a1", Marker, callback385)
	rospy.Subscriber("/track_a2", Marker, callback386)
	print('subscribing to tracka3')
	rospy.Subscriber("/track_a3", Marker, callback387)
	rospy.Subscriber("/track_a4", Marker, callback388)
	rospy.Subscriber("/track_a5", Marker, callback389)
	rospy.Subscriber("/track_a6", Marker, callback390)
	rospy.Subscriber("/track_a7", Marker, callback391)
	rospy.Subscriber("/track_a8", Marker, callback392)
	rospy.Subscriber("/track_a9", Marker, callback393)
	rospy.Subscriber("/track_a10", Marker, callback394)
	rospy.Subscriber("/track_a11", Marker, callback395)
	rospy.Subscriber("/track_a12", Marker, callback396)
	rospy.Subscriber("/track_a13", Marker, callback397)
	rospy.Subscriber("/track_a14", Marker, callback398)
	rospy.Subscriber("/track_a15", Marker, callback399)

	r = rospy.Rate(50)
	# sound()
	printit()
	while not rospy.is_shutdown():
        # print('starting while loop')
		velocity = gnewVel
		print(velocity)
		while not rospy.is_shutdown():
			
			# while not ticker.wait(interval):
				# sound()
				# print(velocity,th)
			# print(velocity)
			now = time.time()
			# if now > reportTime:
			# reportTime = time.time()+df
			# counter += 1
			# print(counter)
			# leadArray.append(leader.get_coords()[1]) #KF of clustered radar measurement
			# vArray.append(velocity)#most recent velocity measurement converted to m/s
			# aArray.append(accel)
			# relvArray.append(myrelv) #do NOT convert to kph
			if velocity > 0:# and (now-validTime < 2):
				th = (leader.get_coords()[0])/(velocity) #distance divided by meters per second
				# print(th)
			else:
				th = -1
			# thArray.append(th)
			# thTime.append(now)
			# twos.append(2)

			leader.predict()
			
			if gnewLeadMeasurement != None:
				
				# print(len(gmyDetections))
				# print('starting cluster if')
				#leadPosition,relv,newVelocity,newAccel = lt.getClusteredRadar(writer = None,recentLeadMeasurement = leadDist,velNaccel= True,gnewLeadMeasurement = gnewLeadMeasurement, gmyDetections = gmyDetections) #0.03 second timeout

				# print(myDetections)
				#cluster 869 and radar points and choose one radar point
				if len(gmyDetections) > 0: #and leadMeasurement != None: # if there are new radar measurements
					# print("inside3 if")
					#radarPlus = np.concatenate((gmyDetections,[[0,gnewLeadMeasurement]]) )#radar measurements plus 869 measurement
					#if len(radarPlus) > 1:
					# print('pre-clustered')
					# print([gnewLeadMeasurement,0],gmyDetections)
					labels = lt.clusterRadar([gnewLeadMeasurement,0],gmyDetections) #cluster algorithm gives labels
					# print('clustered')
					#i869 = labels[-1] #the cluster the 869 measurement is in
					#indices = [i for i, x in enumerate(labels) if x == i869]#find relevant indices of good cluster points
					#indices = np.where(labels == i869)[0] #this should be faster

					myPoints = labels #indices[:-1] #take out 869 from the key points
					# print(myPoints,indices)
					if len(myPoints) > 0: #if there is a point other than from 869 in cluster
						iLead = random.choice(myPoints)#just choose one randomly
						lead = gmyDetections[iLead] #lead coordinates
						# relv = myRelv[iLead] #lead relv
						# print ("lead", lead)
						# print(lead,relv)
						gnewLeadMeasurement = None
						gmyDetections = []#np.empty_like([[0,0]])
						leader.update(lead) #update kf
				myrelv = 0# may be able to add this later (with custom ROS message) relv
				validTime = time.time() #most recent valid measurement from radar
			else:
				if len(gmyDetections) > 64: #and leadMeasurement != None: # if there are new radar measurements
					# print("inside else")
					# print(leader.get_coords().tolist(),gmyDetections)
					labels = lt.clusterRadar(leader.get_coords().tolist(),gmyDetections) #cluster algorithm gives labels
					# print('clustered2')
					#i869 = labels[-1] #the cluster the 869 measurement is in
					#indices = [i for i, x in enumerate(labels) if x == i869]#find relevant indices of good cluster points
					#indices = np.where(labels == i869)[0] #this should be faster

					myPoints = labels #indices[:-1] #take out 869 from the key points
					# print(myPoints,indices)
					if len(myPoints) > 0: #if there is a point other than from 869 in cluster
						iLead = random.choice(myPoints)#just choose one randomly
						lead = gmyDetections[iLead] #lead coordinates
						# relv = myRelv[iLead] #lead relv
						# print ("lead2", lead)
						# print(lead,relv)
						# gnewLeadMeasurement = None
						gmyDetections = []#np.empty_like([[0,0]])
						leader.update(lead) #update kf
        #this controller operates under the assumption that there is a lead vehicle
			velocity = gnewVel
                
		print('before sleep')
		printit.cancel()
		r.sleep()
	print('before spin')
except ValueError:
    print("Oops!  Try again...")