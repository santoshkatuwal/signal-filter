# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 02:37:08 2020

@author: Santosh
"""


import numpy as np
import matplotlib.pyplot as plt
import obspy
import obspy.signal

#edit only data path, and fmin and fmax value

#to create .su file, edit .saf file on np++ (note: edit heading with care)
#import .saf to geopsy and file> export> .su

#reading signal file using obspy library
st = obspy.read("C:\\PTN1504250611.su")

#reading first column data to count number of data
data = st[0].data
npts = len(data)

#reading sample rate from heading
samprate = st[0].stats.sampling_rate

# Filtering the Stream object
st_filt = st.copy()
fmin=0.1    #defining lower frequency
fmax=25      #Defining higher frequency
st_filt.filter('bandpass', freqmin=fmin, freqmax=fmax, corners=2, zerophase=True)

#time calulation
t = np.arange(0, npts / samprate, 1 / samprate)

#Plot of recorded signal
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t,st[0].data,lw=0.5)
plt.subplot(3,1,2)
plt.plot(t,st[1].data,lw=0.5)
plt.subplot(3,1,3)
plt.plot(t,st[2].data,lw=0.5)

#plot of filtered signal
plt.figure(2)
plt.subplot(3,1,1)
plt.plot(t,st_filt[0].data,lw=0.5)
plt.subplot(3,1,2)
plt.plot(t,st_filt[1].data,lw=0.5)
plt.subplot(3,1,3)
plt.plot(t,st_filt[2].data,lw=0.5)