
%pylab inline
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from StringIO import StringIO

#Creating blob parameters
class Blob(): 
    def __init__(self): 
        #construct an empty blob
        self.blobs = []
        self.mass = 0
    def add(self, i, j): 
        #add a pixel at location (i,j) to the blob
        self.blobs.append((i,j));
    def mass(self): 
        #return number of pixels added, which equals the blob's mass
        self.mass = len(self.blobs)
    def distanceTo(self, center_of_mass1, center_of_mass2): 
        #return distance between centers of masses of this blob and blob b
        x1 = center_of_mass1[0]
        x2 = center_of_mass1[1]
        y1 = center_of_mass2[0]
        y2 = center_of_mass2[1]
        
        self.distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return self.distance
    
    def centerOfMass(self): 
        #return touples of x,y values
        total = []
        x_total = 0
        y_total = 0
        for location in self.blobs:
            x_total += location[0]
            y_total += location[1]
        list_of_x = float(x_total)/len(self.blobs)
        list_of_y = float(y_total)/len(self.blobs)
        self.ceterOfMass = [list_of_x, list_of_y]
        return [list_of_x, list_of_y]
    
def count(picture): 
    """Scan the image top to bottom and left to right using a nested loop. 
    When black pixel is found, incriment the count, then call the fill 
    function to fill in all the pixels conected to that one. Pixels are then
    put into the blob in the fill function."""
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK: 
                result += 1
                #making a new blob, getting it's mass, center, filling
                # and adding it to a list of blobs
                blob2 = Blob()
                fill(temp,xsize,ysize,x,y,a_blob)
                a_blob.mass()
                a_blob.centerOfMass()
                list_of_blobs.append(a_blob)
    return list_of_blobs
        
    
def fill(picture, xsize, ysize, xstart, ystart, current_blob):
    """keep a list of pixels that need to be looked at, but haven't 
    yet been filled in - a list of the (x,y) coordinates of pixels that 
    are neighbors of ones we have already examined.  Keep looping until 
    there's nothing left in this list"""
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    queue = [(xstart,ystart)]
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
            #adds red points to the blob in question
            current_blob.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
                
            
def monochrome(picture, tau): #taken from counting stars tour
    """loops over the pixels in the loaded image, 
    replacing the RGB values of each with either 
    black or white depending on whether its total 
    luminance is above or below some threshold 
    passed in by the user"""
    black = (0, 0, 0)
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= threshold: 
                temp[x,y] = black
            else:
                temp[x,y] = white
                
def BlobFinder(picture, tau):
    '''find all blobs in the picture using the luminance threshold tau'''
    float(tau)
    list_of_blobs = []
    monochrome(picture,tau)
    every_blob = count(picture, fill, list_of_blobs)
    return every_blob

def countBeads(P, list_of_blobs):
    '''return the number of beads with >= P pixels'''
    tally = 0
    for b in list_of_blobs: 
        if b.mass >= P: 
            tally += 1
    return tally
    

def getBeads(P, list_of_blobs):
    '''return all beads with >= P pixels'''
    conditional_list_of_blobs = []
    for b in list_of_blobs: 
        if b.mass >= 25:
            conditional_list_of_blobs.append(b)
    return conditional_list_of_blobs