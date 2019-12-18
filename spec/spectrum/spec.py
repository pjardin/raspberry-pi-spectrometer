import cv2
import numpy as np
import time

im = cv2.imread('spec.png')


w = 600
h = 200
x = 470
y = 250

cv2.imshow("blank_image", im)

"""
im = im[y:y+h, x:x + w]


gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Basic threshold example
th, dst = cv2.threshold(gray_image, 70, 255, cv2.THRESH_BINARY);

start = [0,0]
end = [0,0]

for col in range(0,len(dst[0])):
	
	pix = []

	for row in range(0,len(dst)):
		if dst[row][col] != 0:	
			pix.append(row)
	if start == [0,0] and len(pix) != 0:
		top = pix[0]
		bottom = pix[-1]

		r = int(top + (bottom - top)/2)
	
		start = [col, r]
	elif start != [0,0] and len(pix) != 0:
		top = pix[0]
		bottom = pix[-1]

		r = int(top + (bottom - top)/2)
	
		end = [col, r]

 
res = cv2.bitwise_and(im, im,mask = dst)



m = float( (start[1]-end[1])/(start[0]-end[0]))

c = start[1] - m*start[0]

spectrum = []
for x in range(start[0], end[0] + 1 ):
	y = int(m*x + c)
	#cv2.circle(res, (x, y), 5, (255,255,255), -1)
	spectrum.append(im[y][x])



blank_image = np.zeros((200,len(spectrum),3), np.uint8)


for x,s in enumerate(spectrum):
	for y  in range(200):
		blank_image[y][x] = s



cv2.imshow("blank_image", blank_image)
cv2.imwrite('Sdirt.png', blank_image)
"""
print(len(spectrum))


cv2.waitKey(0)

