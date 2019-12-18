import sys
import os
import traceback
import optparse
import time
import logging

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

from detect_peaks import detect_peaks
#https://blog.ytotech.com/2015/11/01/findpeaks-in-python/

#www.noah.org/wiki/wavelength_to_rgb_in)python
def nm_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    """
    R *= 255
    G *= 255
    B *= 255"""
    return (int(R), int(G), int(B))

img = mpimg.imread("/Users/pascaljardin/Desktop/spectrum/spec.png")

height, width, length = img.shape

r, g, b, a = img[0][0]

spec = np.empty((0))
for x in range(width):
    [r,g,b,a] = img[400, x]
    intensity = (int(r*255)+int(g*255)+int(b*255))/3.0
    spec = np.append(spec, intensity)
    
spec = spec - min(spec)

indexes = detect_peaks(spec, mph=150, mpd=1)

peaks = []
largest = 0
for i in indexes:
    if i > 400:
        peaks.append(i)

        if largest == 0:
            largest = i

        if spec[largest] < spec[i]:
            largest = i

indexes = detect_peaks(spec, mph=0, mpd=1)

l = 0
for i in indexes:
    if i > 1200:

        if l == 0:
            l = i
        
        if spec[l] < spec[i]:
            l = i

x1 = peaks[0]
#x2 = largest
x2 = l

y1 = 404.65650
y2 = 763.5106#763.5106

#y - y1 = m(x - x1)
#y = mx -mx1 +y1
#y = mx +c
m = (y2-y1)/(x2-x1)
c = -m*x1 +y1

specArray = []

for x, s in enumerate(spec):
    nm = m*x +c
    if nm > 370:
        specArray.append([nm, s])


res = specArray[1][0]-specArray[0][0]

print(res)

for p in peaks:
    print(m*p +c)

spectrum = np.array(specArray)
x, y = spectrum.T
plt.plot(x, y)
"""
plt.plot(spec)"""
plt.show()








