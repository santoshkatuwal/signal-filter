# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:05:39 2020

@author: Santosh
"""

import numpy as np
import matplotlib.pyplot as plt
import obspy

#edit only data path and fr value

#to create .su file, edit .saf file on np++ (note: edit heading with care)
#import .saf to geopsy and file> export> .su

#reading signal file using obspy library
st = obspy.read("C:\\Users\\Santosh\\Desktop\\Earthquake Signal processing\\PTN1504250611.su")

#reading first column data to count number of data
data = st[0].data
npts = len(data)

#reading sample rate from heading
samprate = st[0].stats.sampling_rate

# Filtering the Stream object
st_filt = st.copy()
fr=1    #defining frequency 

st_filt.filter('lowpass', freq=fr, corners=2, zerophase=True)

#time calulation
t = np.arange(0, npts / samprate, 1 / samprate)

#plot of filtered signal
plt.figure(2)
plt.subplot(3,1,1)
plt.plot(t,st_filt[0].data,lw=0.5)
plt.subplot(3,1,2)
plt.plot(t,st_filt[1].data,lw=0.5)
plt.subplot(3,1,3)
plt.plot(t,st_filt[2].data,lw=0.5)